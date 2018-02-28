var $$=Dom7;var iCloudDNSBypass=new Framework7();var mainView=iCloudDNSBypass.addView('.view-main',{dynamicNavbar:true});iCloudDNSBypass.onPageAfterAnimation('www',function(page)
{function Validate(Url)
{var Domain=/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{1,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/;
var IP=/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}[\s\S]{0,}/;if(!Url.match(Domain)&&!Url.match(IP))
{return false;}
return true;}
$$("#Url").keypress(function(Event)
{if(Event.which==13)
{$$("#Go").trigger("click");}
else
{$$('#Error').hide();}});$$("#Go").on('click',function()
{var Url=$$('#Url').val();var Redirect='http://ui.iclouddnsbypass.com/deviceservices/buddy/barney_activation_help_en_us.buddyml?redirect=';if(Url.substring(0,5)!='http:'&&Url.substring(0,6)!='https:')
{Url='http://'+Url;}
if(!Validate(Url))
{$$('#Error').show();}
else
{window.location.href=Redirect+encodeURIComponent(Url);}});$$("#Url").focus();});