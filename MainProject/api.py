from .serializer import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .forms import *
from .models import *
from datetime import date,datetime,timedelta
from django.core.mail import send_mail


# def send_email_view(request):
   
@api_view(["GET"])
def getUserData(request):
    user = UserSerializer(request.user).data
    return JsonResponse({'user':user})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getBescData(request):
    besc_data = BesicData.objects.first()
    return JsonResponse({'data':BescDataSirializer(besc_data).data})

@api_view(['POST'])
def Setting(request):
    basc_data = BesicData.objects.first()
    # print(basc_data)
    if basc_data:
        form = BesicDataForm(request.data or None,instance=basc_data)
    else:
        form = BesicDataForm(request.data or None)
    
    if form.is_valid():
        basc_data = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    
    return JsonResponse({'status':True,'data':BescDataSirializer(basc_data).data})

@api_view(['POST'])
def create_organizers(request):
    form = OrganizersForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':OrganizersSerializer(organizers).data})

@api_view(['POST'])
def update_organizers(request,id):
    organizers = Organizers.objects.get(pk=id)
    
    form = OrganizersForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':OrganizersSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_organizers(request):
    besc_data = Organizers.objects.all()
    return JsonResponse({'data':OrganizersSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_organizer(request,id):
    besc_data = Organizers.objects.get(pk=id)
    return JsonResponse({'data':OrganizersSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_organizer(request,id):
    besc_data = Organizers.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})

# ======================================= #

@api_view(['POST'])
def create_shepherds(request):
    form = ShepherdsForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ShepherdsSerializer(organizers).data})

@api_view(['POST'])
def update_shepherds(request,id):
    organizers = Shepherds.objects.get(pk=id)
    
    form = ShepherdsForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ShepherdsSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_shepherds(request):
    besc_data = Shepherds.objects.all()
    return JsonResponse({'data':ShepherdsSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_shepherd(request,id):
    besc_data = Shepherds.objects.get(pk=id)
    return JsonResponse({'data':ShepherdsSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_shepherds(request,id):
    besc_data = Shepherds.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})

# ====================== Schedule ========================== #

@api_view(['POST'])
def create_schedule(request):
    form = ScheduleForm(request.data,request.FILES)
    
    if form.is_valid():
        schedule = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ScheduleSirializer(schedule).data})

# @api_view(['POST'])
# def update_schedule(request,id):
#     organizers = Schedule.objects.get(pk=id)
    
#     form = ShepherdsForm(request.data,request.FILES,instance=organizers)
    
#     if form.is_valid():
#         new_organizers = form.save()
#     else:
#         return JsonResponse({'status':False,'error':form.errors})
#     return JsonResponse({'status':True,'data':ShepherdsSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_schedule(request):
    besc_data = Schedule.objects.all()
    settings = BesicData.objects.first()
    array_of_dates = []
    if settings:
        d1 = settings.from_date
        d2 = settings.to_date
        result1 = abs(d2-d1).days + 1
        print(result1)
        for i in range(0,result1):
            array_of_dates.append(d1+timedelta(days=i))
    
    return JsonResponse({'data':ScheduleSirializer(besc_data,many=True).data,'days':array_of_dates})

@api_view(['DELETE'])
def delete_schedule(request,id):
    besc_data = Schedule.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})


# ======================================= #

@api_view(['POST'])
def create_Speakers(request):
    form = SpeakersForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':SpeakersSerializer(organizers).data})

@api_view(['POST'])
def update_Speakers(request,id):
    organizers = Speakers.objects.get(pk=id)
    
    form = SpeakersForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':SpeakersSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_Speakers(request):
    besc_data = Speakers.objects.all()
    return JsonResponse({'data':SpeakersSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_shepherd(request,id):
    besc_data = Speakers.objects.get(pk=id)
    return JsonResponse({'data':SpeakersSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_Speakers(request,id):
    besc_data = Speakers.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])

def all_data(request):
     settings = BesicData.objects.first()
     speakers = Speakers.objects.all()
     shepherds = Shepherds.objects.all()
     schedule = Schedule.objects.all()
     organizers = Organizers.objects.all()
     
     array_of_dates = []
     if settings:
        d1 = settings.from_date
        d2 = settings.to_date
        result1 = abs(d2-d1).days + 1
        print(result1)
        for i in range(0,result1):
            array_of_dates.append(d1+timedelta(days=i))
            
        return JsonResponse({
            'settings':BescDataSirializer(settings).data,
            'speakers':SpeakersSerializer(speakers,many=True).data,
            'schedule':ScheduleSirializer(schedule,many=True).data,
            'shepherds':ShepherdsSerializer(shepherds,many=True).data,
            'organizers':OrganizersSerializer(organizers,many=True).data,
            'day_of_events':array_of_dates
        })
        
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_Booking(request):
    form = BookingForm(request.data,request.FILES)
    
    if form.is_valid():
        booking = Booking.objects.filter(Suite_number=form.cleaned_data.get('Suite_number'),status=2).exists()
        if booking:
            return JsonResponse({'status':False,'error':{'Suite_number':'هذا الموقع محجوز مسبقا'}})
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':BookingSerializer(organizers).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def change_status_booking(request,id):
    booking = Booking.objects.get(pk=id)
    booking2 = Booking.objects.filter(Suite_number=booking.Suite_number,status=2).exists()
    if booking2 and request.GET['status'] == 2:
        return JsonResponse({'status':False,'error':{'Suite_number':'هذا الموقع محجوز مسبقا'}})
    booking.status = request.GET['status']
    booking.save()
    return JsonResponse({'status':True})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_all_booking(request):
    booking = Booking.objects.all()
    
    return JsonResponse({'status':True,'data':BookingSerializer(booking,many=True).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def check_book(request):
    booking = Booking.objects.filter(status=2).values_list('Suite_number', flat=True)
    
    return JsonResponse({'status':True,'data':list(booking)})
    
@api_view(['POST'])
def change_sutter(request):
    id = request.data.get('id')
    Suite_number = request.data.get('Suite_number')
    
    booking = Booking.objects.get(id=id)
    
    booking.Suite_number = Suite_number
    
    booking.save()
    
    return JsonResponse({'status':True})
    
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_project(request):
    form = ProjectForm(request.data,request.FILES)
    
    if form.is_valid():
        
        project = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ProjectSerializer(project).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def change_status_project(request,id):
    project = Project.objects.get(pk=id)
    project.status = request.GET['status']
    project.save()
    b1 = ""
    b2 = ''
    if project.status == 2:
        b1 ='<p>تمت الموافقة على مشروعك من قبل اللجنة المنظمة</p>'
        b2 = "تاكيد الاشتراك"
    elif project.status == 3:
        b1 ='<p>لم تمت الموافقة على مشروعك من قبل اللجنة المنظمة</p>'
        b2 = "ناسف على عدم الموافقة"
    if b1 != '' and b2 != '':
        body = '''<div role="document" tabindex="-1" aria-label="Message body" class="XbIp4 jmmB7 GNqVo allowTextSelection OuGoX"
    id="UniqueMessageBody">
    <div>
        <style>
        p{
         font-weight: bold;
    font-family: system-ui;
    margin:0px;padding:px;   
        }
          
        </style>
        <div class="rps_62be">
            <div lang="EN-US" link="#0563C1" vlink="#954F72" style="word-wrap:break-word;background-color:#fff">
                <div class="x_WordSection1">
                    <p class="x_MsoNormal" aria-hidden="true">&nbsp;</p>
                    <p class="x_MsoNormal" aria-hidden="true">&nbsp;</p>
                    <p class="x_MsoNormal"><b><span
                                style="font-size:12.0pt; color:#FF8E14; background:white">&nbsp;</span></b></p>
                    <p class="x_MsoNormal"><b><span
                                style="font-size:12.0pt; color:#00467D; background:white">&nbsp;</span></b></p>
                    <p class="x_MsoNormal" dir="RTL" style="text-align:right; direction:rtl; unicode-bidi:embed">
                        <b><span lang="AR-LY" style="font-size:12.0pt; color:#222222; background:white">المشارك : '''+project.name+''' </span></b>
                        <span
                            dir="RTL"></span><span dir="RTL"></span><b><span
                                style="font-size:12.0pt; color:#222222; background:white"><span dir="RTL"></span><span
                                    dir="RTL"></span> </span></b><b><span dir="LTR"
                                style="font-size:12.0pt; color:#222222; background:white"></span></b></p>
                    <p class="x_MsoNormal" dir="RTL" style="text-align:right; direction:rtl; unicode-bidi:embed">
                        <b><span lang="AR-LY" style="font-size:12.0pt; color:#222222; background:white">رقم التسجيل : '''+ str(project.id) +'''
                            </span></b></p>
                            <p class="x_MsoNormal" dir="RTL" style="text-align:right; direction:rtl; unicode-bidi:embed">
                        <b><span lang="AR-LY" style="font-size:12.0pt; color:#222222; background:white">المشروع : '''+ project.project_title +'''
                            </span></b></p>
                            <p class="x_MsoNormal" dir="RTL" style="text-align:right; direction:rtl; unicode-bidi:embed">
                        <b><span lang="AR-LY" style="font-size:12.0pt; color:#222222; background:white">''' +b1+ '''
                            </span></b></p>
                    <p class="x_MsoNormal"><b><span lang="HE" dir="RTL"
                                style="font-size:12.0pt; color:#FF8E14; background:white">&nbsp;</span></b></p>
                    <p class="x_MsoNormal" align="right" style="text-align:right"><b><span lang="AR-LY" dir="RTL"
                                style="font-size:12.0pt; color:#222222; background:white">مع اطيب
                                التحيات</span></b><b><span
                                style="font-size:12.0pt; color:#222222; background:white"></span></b></p>
                    <p class="x_MsoNormal" align="right" style="text-align:right"><b><span lang="AR-LY" dir="RTL"
                                style="font-size:12.0pt; color:#222222; background:white">فريق تنظيم ملتقى فزان
                                التقني</span></b></p>
                    <p class="x_MsoNormal" align="right" style="text-align:right"><b><span lang="AR-LY" dir="RTL"
                                style="font-size:12.0pt; color:#222222; background:white">#</span></b><b><span
                                style="font-size:12.0pt; color:#222222; background:white">FezzanTechX</span></b><b><span
                                lang="AR-LY" dir="RTL"
                                style="font-family:&quot;Arial&quot;,sans-serif; color:#222222"></span></b></p>
                    <p class="x_MsoNormal" aria-hidden="true">&nbsp;</p>
                    <table class="x_MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="529"
                        style="width:396.6pt; background:white; border-collapse:collapse">
                        <tbody>
                            <tr style="height:18.9pt">
                                <td width="104" valign="top"
                                    style="width:78.1pt; border:none; border-right:solid #F6AE2D 1.0pt; padding:.75pt 7.5pt .75pt .75pt; height:18.9pt">
                                    <p class="x_MsoNormal"><span style="color:#201F1E"><img
                                                data-imagetype="AttachmentByCid"
                                                originalsrc="cid:image001.png@01DA65C1.62796F70"
                                                data-custom="AAMkADQxOTlhZTc4LWNkYzAtNDRiMS1iMDg0LTMwZjUxYzhjNzAyMABGAAAAAAACHKewdMUuTpk0LHaGZeivBwBi0P%2BdroKbR5BeGFganDWDAAAAAAEMAABi0P%2BdroKbR5BeGFganDWDAAAdTjiAAAABEgAQADIVDhXs09BPp0jnCHSTcos%3D"
                                                naturalheight="0" naturalwidth="0"
                                                src='https://fezzantechx.ly/wp-content/uploads/2024/02/Asset-18-1024x449.png'
                                                width="301" height="132" id="x__x0635__x0648__x0631__x0629__x0020_1"
                                                style="width: 3.1354in; height: 1.375in; cursor: pointer; min-height: auto; min-width: auto;"
                                                crossorigin="use-credentials" fetchpriority="high"
                                                class="Do8Zj"></span><span style=""></span></p>
                                </td>
                                <td width="425" style="width:318.5pt; padding:.75pt .75pt .75pt 7.5pt; height:18.9pt">
                                    <table class="x_MsoNormalTable" border="0" cellspacing="0" cellpadding="0"
                                        style="border-collapse:collapse">
                                        <tbody>
                                            <tr style="height:17.25pt">
                                                <td width="273" valign="top"
                                                    style="width:204.6pt; padding:.75pt .75pt 3.75pt 7.5pt; height:17.25pt">
                                                    <p class="x_MsoNormal"><b><span
                                                                style="font-size:16.0pt; font-family:Roboto; color:#222222">Fezzan
                                                                Tech Expo</span></b><span
                                                            style="font-size:16.0pt; font-family:Roboto; color:#222222"></span>
                                                    </p>
                                                </td>
                                                <td width="141" valign="top"
                                                    style="width:105.65pt; padding:.75pt .75pt 3.75pt 7.5pt; height:17.25pt">
                                                </td>
                                            </tr>
                                            <tr style="height:58.5pt">
                                                <td width="273" valign="top"
                                                    style="width:204.6pt; padding:3.75pt .75pt 3.75pt 7.5pt; height:58.5pt">
                                                    <p class="x_MsoNormal" style="line-height:12.75pt"><b><span
                                                                style="font-size:12.0pt; color:#222222">E:</span></b><span
                                                            style="font-size:12.0pt; color:#222222">&nbsp;<a
                                                                href="mailto:info@zallaf.ly" data-linkindex="0"><span
                                                                    style="color:#222222">info@fezzantechx.ly</span><span
                                                                    style="color:#222222"></span></a></span></p>
                                                    <p class="x_MsoNormal" style="line-height:12.75pt"><b><span
                                                                style="font-size:12.0pt; color:#222222">W:</span></b><u><span
                                                                style="font-size:12.0pt; color:#222222"><a
                                                                    href="http://&nbsp;www.fezzantechx.ly"
                                                                    target="_blank" rel="noopener noreferrer"
                                                                    data-auth="NotApplicable" data-linkindex="1"><span
                                                                        style="color:#222222">&nbsp;www.fezzantechx.ly</span></a></span></u><span
                                                            style="font-size:12.0pt; color:#222222"></span></p>
                                                    <p class="x_MsoNormal" style="line-height:12.75pt"><b><span
                                                                style="font-size:12.0pt; color:#222222; background:white">MO:</span></b><span
                                                            style="font-size:12.0pt; color:#222222; background:white">&nbsp;218-925315300.</span><span
                                                            style="color:#222222"></span></p>
                                                </td>
                                                <td width="141"
                                                    style="width:105.65pt; padding:.75pt .75pt .75pt .75pt; height:58.5pt">
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="x_MsoNormal" aria-hidden="true">&nbsp;</p>
                    <p class="x_MsoNormal" aria-hidden="true">&nbsp;</p>
                </div>
            </div>
        </div>
    </div>
</div>'''
        send_mail(b2, '', 'info@fezzantechx.ly', [project.email],html_message=body)
    return JsonResponse({'status':True,'st':project.status})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_all_project(request):
    
    project = Project.objects.all()
    
    return JsonResponse({'status':True,'data':ProjectSerializer(project,many=True).data})

import random
import segno
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_Gustis(request):
    form = GustisForm(request.data,request.FILES)
    if form.is_valid():
        check = True
        while(check):
            rand = "FZ"+str(random.randrange(10,9999))
            check = Gustis.objects.filter(id_user = rand).exists()
        gustis = form.save(commit=False)
        gustis.id_user = rand
        gustis.save()
    else:
        gustis = Gustis.objects.filter(phone=request.data.get('phone')).first()
        return JsonResponse({'status':False,'error':form.errors,'data':GustisSerializer(gustis).data})
    return JsonResponse({'status':True,'data':GustisSerializer(gustis).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def change_status_Gustis(request,id):
    gustis =Gustis.objects.get(pk=id)
    gustis.status = request.GET['status']
    gustis.save()
    return JsonResponse({'status':True})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_all_Gustis(request):
    
    gustis = Gustis.objects.all()
    
    return JsonResponse({'status':True,'data':GustisSerializer(gustis,many=True).data})


@api_view(['POST'])
def create_clouds(request):
    form = CloudsForm(request.data or None)
    if form.is_valid():
        cloud = form.save()
        return JsonResponse({'status':True,'data':CloudsSerializer(cloud).data})
    else:
        return JsonResponse({'status':False,'error':form.errors})
        
@api_view(['POST'])
def change_status_clouds(request):
    status = request.data.get('status')
    id = request.data.get('id')
    print(id)
    cloud = Clouds.objects.get(pk=id)
    cloud.status = status
    cloud.save()
    return JsonResponse({'status':True,'data':CloudsSerializer(cloud).data})
    
@api_view(['GET'])
def get_clouds(request):
    clouds = Clouds.objects.all()
    return JsonResponse({'status':True,'data':CloudsSerializer(clouds,many=True).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_cloud(request,id):
    cloud = Clouds.objects.get(pk=id)
    return JsonResponse({'status':True,"data":CloudsSerializer(cloud).data})

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_cloud_guist(request):
    cloud = request.data.get('cloud')
    gust = request.data.get('gust')
    if not CloudsGustis.objects.filter(clouds=cloud,gusti=gust).exists():
        cloud = Clouds.objects.get(pk=cloud)
        gust = Gustis.objects.get(pk=gust)
        cl_gus = CloudsGustis.objects.create(clouds=cloud,gusti=gust)
        return JsonResponse({'status':True,'data':CloudsGustiSerializer(cl_gus).data})
    else:
        cl_gus = CloudsGustis.objects.filter(clouds=cloud,gusti=gust).first()
        return JsonResponse({'status':False,'message':f'انت مسجل مسبقا باسم : { cl_gus.gusti.name } '})
    
    
import random
import segno
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_Player(request):
    form = PlayersForm(request.data,request.FILES)
    if form.is_valid():
        player = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':PlayersSerializer(player).data})

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_all_Player(request):
    
    player = Players.objects.all()
    
    return JsonResponse({'status':True,'data':PlayersSerializer(player,many=True).data})
