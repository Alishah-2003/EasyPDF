from django.shortcuts import render, redirect, get_object_or_404
from uploadfile.models import PDFUpload, SharePDF, CommentPDF
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages

@login_required
def upload_file(request):
    if request.method == "POST":
        if 'upload_file' not in request.FILES:
            return render(request, "uploadfile/uploadfiles.html", {
                "error": "No such file found, please upload the file."
            })
        
        uploadedFile = request.FILES['upload_file']
        if not uploadedFile.name.endswith('.pdf'):
            return render(request, "uploadfile/uploadfiles.html", {
                "error": "The uploaded file is not in PDF format"
            })
        filename=request.POST.get('filename')
        pdf_obj = PDFUpload.objects.create(
            user = request.user,
            name = request.POST.get('filename'),
            file_uploaded = uploadedFile   
        )
        SharePDF.objects.create(pdf=pdf_obj)
        messages.success(request, f'File "{filename}" has been successfully uploaded! You can view your file in "View All PDFs"')
                                
        return redirect("/uploadfile/")
    else:
        return render(request,"uploadfile/uploadfiles.html")


@login_required
def dashboard_view(request):
    return render(request,"uploadfile/dashboard.html")


@login_required
def view_share_pdf(request):
    files_uploaded = PDFUpload.objects.filter(user=request.user).order_by('-upload_time')

    for pdf in files_uploaded:
        SharePDF.objects.get_or_create(pdf=pdf)

    search_file = request.GET.get('searched','')
    if search_file:
        files_uploaded = files_uploaded.filter(Q(name__icontains=search_file)|Q(file_uploaded__icontains=search_file))

    return render(request,"uploadfile/viewallpdfs.html", {
        'view_pdfs':files_uploaded,
        'search_query':search_file
    })

@login_required
def select_share(request):
    pdfs=PDFUpload.objects.filter(user=request.user)
    return render(request,"uploadfile/select_share.html", {
        'pdfs':pdfs
    })

@login_required
def generate_link(request,pdf_id):
    pdf=get_object_or_404(PDFUpload, id=pdf_id, user=request.user)
    share_link, created = SharePDF.objects.get_or_create(pdf=pdf)
    share_url=request.build_absolute_uri(f'uploadfile/share_file/{share_link.link}/')

    return render(request,"uploadfile/sharefile.html", {
        'pdf': pdf,
        'share_url': share_url,
        'all_comments': CommentPDF.objects.filter(pdf=pdf)
    })

@csrf_exempt
@require_http_methods(["GET","POST"])
def share_file(request, link):
    shared_pdf = get_object_or_404(SharePDF, link=link)
    pdf=shared_pdf.pdf
    share_url = request.build_absolute_uri(f'/share_file/{link}/')

    if request.method=="POST":
        comment_text = request.POST.get('comment')
        given_name = request.POST.get('given_name','Anonymous')

        if not comment_text:
            return render(request,"uploadfile/sharefile.html",{
                'pdf':pdf,
                'share_url':share_url,
                'all_comments':CommentPDF.objects.filter(pdf=pdf),
                'error':'Comment cannot be empty'

            })
        if request.user.is_authenticated:
            commenter=f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username
        else:
            commenter= given_name if given_name else "Anonymous"
        
        CommentPDF.objects.create(
            pdf=pdf,
            commenter=commenter,
            comment=comment_text.strip()
        )
        return redirect('share_file',link=link)

    all_comments = CommentPDF.objects.filter(pdf=pdf)
    return render(request,"uploadfile/sharefile.html", {
        'pdf':pdf,
        'all_comments':all_comments,
        'share_url': share_url,
    })



