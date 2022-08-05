from django.shortcuts import render, redirect
from requests import delete
from .models import User, Keyword, Frame
from .froms import PostFrame
from django.contrib import messages
# Create your views here.

def frame(request):
    if request.user.is_authenticated:
        like = request.user.likeMany.all()
        save = request.user.saveMany.all()
    else:
        like = None
        save = None
    keywordinfo = Keyword.objects.all()

    query = request.GET.get('title', None)
    if query:
        frameinfo = Frame.objects.filter(frametitle__contains=query)
    else:
        frameinfo = Frame.objects.all()
        
    likereq = request.GET.get('like',None)
    savereq = request.GET.get('save',None)
    querykeyword = request.GET.get('sortkeyword',"None")
    if querykeyword != "None":
        frameinfo = Frame.objects.filter(framekeyword__id__contains=querykeyword)
        querykeyword = int(querykeyword)
    else:
        frameinfo = Frame.objects.all()
    if likereq != None:
        sltframe = Frame.objects.filter(id = likereq)
        if request.user in sltframe[0].framelikeuser.all():
            sltframe[0].framelikeuser.remove(request.user)
        else:
            sltframe[0].framelikeuser.add(request.user)
        sltframe[0].save()

    if savereq != None:
        sltframe = Frame.objects.filter(id = savereq)
        if request.user in sltframe[0].framesaveuser.all():
            sltframe[0].framesaveuser.remove(request.user)
        else:
            sltframe[0].framesaveuser.add(request.user)
        sltframe[0].save()
    context = {
        "frameinfo": frameinfo,
        "like": like,
        "save": save,
        "keywordinfo": keywordinfo,
        "querykeyword": querykeyword
    }

    return render(request, template_name='framesharings/frame.html',context=context)


def framedetail(request,id):
    frameinfo = Frame.objects.get(id =id)
    keywordinfo = Keyword.objects.all()
    like = request.user.likeMany.all()
    save = request.user.saveMany.all()
    likereq = request.GET.get('like',None)
    savereq = request.GET.get('save',None)
    if likereq != None:
        sltframe = Frame.objects.filter(id = likereq)
        if request.user in sltframe[0].framelikeuser.all():
            sltframe[0].framelikeuser.remove(request.user)
        else:
            sltframe[0].framelikeuser.add(request.user)
        sltframe[0].save()

    if savereq != None:
        sltframe = Frame.objects.filter(id = savereq)
        if request.user in sltframe[0].framesaveuser.all():
            sltframe[0].framesaveuser.remove(request.user)
        else:
            sltframe[0].framesaveuser.add(request.user)
        sltframe[0].save()

    context = {
        "frameinfo": frameinfo,
        "keywordinfo": keywordinfo,
        "like": like,
        "save": save,
    }
    return render(request, template_name="framesharings/framedetail.html", context=context)

def framecreate(request):
    keywordinfo = Keyword.objects.all()
    # form = PostFrame()

    if request.method == "POST":
        
        framephoto = request.FILES.get("framephoto")
        if framephoto == None:
            messages.warning(request, '사진은 필수입니다.')
            return redirect("framesharings:framecreate")
        
        frametitle = request.POST["frametitle"]
        frameexample = request.FILES.get("frameexamle")
        framememo = request.POST["framememo"]
        framepublic = request.POST.get("framepublic")
        userid = User.objects.get(id = request.user.id)
        if framepublic == "False":
            Frame.objects.create(framememo=framememo,framephoto=framephoto, frametitle=frametitle,frameexample=frameexample,userid=userid,framepublic=False)
        else:
            Frame.objects.create(framememo=framememo,framephoto=framephoto, frametitle=frametitle,frameexample=frameexample,userid=userid,framepublic=True)
        a = Frame.objects.all()
        keywordoj = a.last()
        for i in range(1,len(keywordinfo)+1):
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.framekeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()
            
        
        return redirect(f"/framedetail/{a.last().id}")
        
    context = {
        "keywordinfo": keywordinfo,
        # "form": form
    }
    return render(request, template_name="framesharings/framecreate.html",context=context)

def frameupdate(request,id):
    keywordinfo = Keyword.objects.all()
    if request.method == "POST":
        framephoto = request.FILES.get("framephoto")
        frametitle = request.POST["frametitle"]
        frameexample = request.FILES.get("frameexamle")
        framememo = request.POST["framememo"]
        framepublic = request.POST.get("framepublic")
        if framepublic == "False":
            decision = False
        else:
            decision = True
        userid = User.objects.get(id = request.user.id)
        clearphoto = request.POST.get("clearphoto")
        clearexample = request.POST.get("clearexample")

        if framephoto == None and frameexample == None:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)

            else :
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)


        elif framephoto and frameexample == None:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=None,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)

            else :
                Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=Frame.objects.filter(id = id)[0].frameexample,framememo=framememo,framepublic=decision,)


        elif framephoto == None and frameexample:
            if clearphoto == 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)

            elif clearphoto != 'clearphoto' and clearexample == 'clearexample':
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)

            elif clearphoto == 'clearphoto' and clearexample != 'clearexample':
                Frame.objects.create(userid = userid, framephoto = None,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)
            else :
                Frame.objects.create(userid = userid, framephoto = Frame.objects.filter(id = id)[0].framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)
        else:
            Frame.objects.create(userid = userid, framephoto = framephoto,frametitle=frametitle,frameexample=frameexample,framememo=framememo,framepublic=decision,)


        




        Frame.objects.filter(id=id).delete()
        a = Frame.objects.all()
        keywordoj = a.last()
        for i in range(1,len(keywordinfo)+1):
            keywordap = request.POST.get(str(i))
            if keywordap:
                keywordoj.framekeyword.add(Keyword.objects.filter(id = i)[0])
        keywordoj.save()
            
        
        return redirect(f"/framedetail/{a.last().id}")

    frameinfo = Frame.objects.get(id = id)
    context = {
        "frameinfo": frameinfo,
        "keywordinfo": keywordinfo,
    }
    return render(request, template_name="framesharings/frameupdate.html", context=context)

def framedelete(request,id):
    if request.method == "POST":
        Frame.objects.filter(id=id).delete()
        return redirect("/frame")