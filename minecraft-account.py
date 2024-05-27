

<!DOCTYPE html>
<html lang="en">
<head id="head"><meta charset="utf-8" /><meta lang="en"/>
<script>
    (function (w) {
        w.wasStartupInvoked = true;
        var f = w.Filemail = w.Filemail || {};
        f.apiSetup = { baseUrl: 'https://api.filemail.com', version: '2.0' };
        f.appver = '1.9658.1641-a48987b';
        f.env = 'Production';
        f.scriptsVer = '1.9658.1641.1';
        f.logenabled = false;
        f.pages = f.pages || {};
        f.ng = f.ng || {};
        f.datez = { firstDayOfWeek: 0 };
        f.defaultCulture = 'en-us';
        f.culture = 'en-us';
        f.currentUrlLanguagePart = '';
        f.b64decode = function (str) { return decodeURIComponent(atob(str).split('').map(function (c) { return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2); }).join('')); };
        f.colors = { primary: '#1377C3' };
        var config = JSON.parse(Filemail.b64decode('eyJmYmlkIjoiMTM4MzAwMDMyMDk2IiwiY2RuIjoiIiwiY291bnRyeSI6IkJFIiwibWVtYmVyc2hpcCI6IkZyZWUiLCJ1cGxvYWRlclVzZXIiOm51bGwsIm1heEZyZWVUcmFuc2ZlcnNQZXIyNEgiOjJ9'));
        w.FacebookAppId = config.fbid;
        f.uploader = f.uploader || {};
        f.uploader.user = config.uploaderUser;
        f.Country = config.country;
        f.Settings = { MaxFreeTransfersPer24Hours: 2 };
        f.CDN = config.cdn;
        
        f.OSdetect = (function () {
            var macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
                windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
                iosPlatforms = ['iPhone', 'iPad', 'iPod'];
            var ua = (w.navigator.userAgent || '').toLowerCase(), pl = w.navigator.platform, os = null;
            if (ua.indexOf('iphone') > -1 || ua.indexOf('ipad') > -1 || ua.indexOf('macintosh') > -1 && 'ontouchend' in document) {
                os = 'iOS';
            } else if (macosPlatforms.indexOf(pl) !== -1) {
                os = 'Mac OS';
            } else if (windowsPlatforms.indexOf(pl) !== -1) {
                os = 'Windows';
            } else if (/android/.test(ua)) {
                os = 'Android';
            }
            if (!os && /Linux/.test(pl)) {
                os = 'Linux';
            }
            return os;
        })();
        
        f.deeplinkHost = 'https://deeplink.filemail.com';
    })(window);

    var _mtm = window._mtm = window._mtm || [];
    var _paq = window._paq = window._paq || [];
    _mtm.push({'mtm.startTime': (new Date().getTime()), 'event': 'mtm.Start'});
    (function() {
        var d=document,s=d.getElementsByTagName('script')[0],t=d.createElement('script');
        t.async=true; t.src='https://analytics.filemail.com/js/container_UpE19V8Y.js'; s.parentNode.insertBefore(t,s);
    })();

</script><meta name="copyright" content="Filemail" /><meta name="author" content="Filemail" /><meta name="Distribution" content="Global" /><meta name="Rating" content="General" /><meta name="robots" content="noindex"/><meta name="Revisit-after" content="1 Day" /><meta name="verify-v1" content="MTKk0EcIWNVD3zEsTmhv++t10WKbcZk+aCWikyqyRGw=" /><meta name="theme-color" content="#1377C3" /><meta name="twitter:card" content="summary" /><meta name="twitter:site" content="@filemail" /><meta property="og:site_name" content="Filemail" /><meta property="og:type" content="website" /><title>
	Longfen1760 - Download files
</title><meta name="description" content="Click here to view and download these shared files from Filemail.com"><meta itemprop="description" content="Click here to view and download these shared files from Filemail.com"><meta property="og:description" content="Click here to view and download these shared files from Filemail.com"><meta name="twitter:description" content="Click here to view and download these shared files from Filemail.com"><meta property="og:image" content="https://filemailprod.blob.core.windows.net/images/filemailLogoBlue.png"><meta itemprop="image" content="https://filemailprod.blob.core.windows.net/images/filemailLogoBlue.png"><meta property="og:title" content="Longfen1760 - Download files"><meta name="twitter:title" content="Longfen1760 - Download files"><meta itemprop="name" content="Longfen1760 - Download files"><meta property="fb:app_id" content="138300032096">
<link href="/Frontend/css/fontspreload.css" rel="preload stylesheet" as="style">
<style>
@font-face {font-family: 'Font Awesome 5 Pro';font-style: normal;font-weight: 300;font-display: swap; src: url('/Frontend/fontawesome/webfonts/fa-light-300.eot');src: url('/Frontend/fontawesome/webfonts/fa-light-300.eot?#iefix') format('embedded-opentype'), url('/Frontend/fontawesome/webfonts/fa-light-300.woff2') format('woff2'), url('/Frontend/fontawesome/webfonts/fa-light-300.woff') format('woff'), url('/Frontend/fontawesome/webfonts/fa-light-300.ttf') format('truetype'), url('/Frontend/fontawesome/webfonts/fa-light-300.svg#fontawesome') format('svg');}
.fal, .fas {font-family: 'Font Awesome 5 Pro';font-weight: 300;}
@font-face { font-family: 'Font Awesome 5 Pro Brands'; font-style: normal; font-weight: 400; font-display: swap; src: url('/Frontend/fontawesome/webfonts/fa-brands-400.eot'); src: url('/Frontend/fontawesome/webfonts/fa-brands-400.eot?#iefix') format('embedded-opentype'), url('/Frontend/fontawesome/webfonts/fa-brands-400.woff2') format('woff2'), url('/Frontend/fontawesome/webfonts/fa-brands-400.woff') format('woff'), url('/Frontend/fontawesome/webfonts/fa-brands-400.ttf') format('truetype'), url('/Frontend/fontawesome/webfonts/fa-brands-400.svg#fontawesome') format('svg'); }
.fab { font-family: 'Font Awesome 5 Pro Brands'; font-weight: 400; }
@font-face {font-family: 'dotsfont';font-display: auto;src: url('/Frontend/fonts/dotsfont.eot');src: url('/Frontend/fonts/dotsfont.eot?#iefix') format('embedded-opentype'), url('/Frontend/fonts/dotsfont.woff') format('woff'), url('/Frontend/fonts/dotsfont.ttf') format('truetype'), url('/Frontend/fonts/dotsfont.svg#dotsfontregular') format('svg');}
.conceal{font-family:'dotsfont';}
</style>
<meta name="google-play-app" content="app-id=no.degree.filemail.app" /><meta name="p:domain_verify" content="0ddce08b74782997db6e5fd7a25661dd" /><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" /><meta name="format-detection" content="telephone=no" /><link rel="icon" type="image/png" sizes="32x32" href="/images/favicons/favicon-32x32.png" /><link rel="icon" type="image/png" sizes="16x16" href="/images/favicons/favicon-16x16.png" /><link rel="shortcut icon" href="/images/favicons/favicon.ico" /><link rel="mask-icon" href="/images/favicons/safari-pinned-tab.svg" color="#5bbad5" /><link rel="manifest" href="/images/favicons/site.webmanifest" /><link rel="apple-touch-icon" sizes="180x180" href="/images/favicons/apple-touch-icon.png" />
        
        <style>*,::after,::before{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-webkit-tap-highlight-color:transparent}article,aside,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}body{margin:0;font-family:Lato,Arial,Helvetica,sans-serif;font-size:1rem;font-weight:400;line-height:1.5;color:#212529;text-align:left;background-color:#fff}[tabindex="-1"]:focus:not(:focus-visible){outline:0!important}hr{box-sizing:content-box;height:0;overflow:visible}h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:.5rem}p{margin-top:0;margin-bottom:1rem}abbr[data-original-title],abbr[title]{text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted;cursor:help;border-bottom:0;-webkit-text-decoration-skip-ink:none;text-decoration-skip-ink:none}address{margin-bottom:1rem;font-style:normal;line-height:inherit}dl,ol,ul{margin-top:0;margin-bottom:1rem}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}dt{font-weight:700}dd{margin-bottom:.5rem;margin-left:0}blockquote{margin:0 0 1rem}b,strong{font-weight:bolder}small{font-size:80%}sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}a{color:#1377c3;text-decoration:none;background-color:transparent}a:hover{color:#0c4c7d;text-decoration:underline}a:not([href]){color:inherit;text-decoration:none}a:not([href]):hover{color:inherit;text-decoration:none}code,kbd,pre,samp{font-family:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:1em}pre{margin-top:0;margin-bottom:1rem;overflow:auto;-ms-overflow-style:scrollbar}figure{margin:0 0 1rem}img{vertical-align:middle;border-style:none}svg{overflow:hidden;vertical-align:middle}table{border-collapse:collapse}caption{padding-top:.75rem;padding-bottom:.75rem;color:#6c757d;text-align:left;caption-side:bottom}th{text-align:inherit}label{display:inline-block;margin-bottom:.5rem}button{border-radius:0}button:focus{outline:1px dotted;outline:5px auto -webkit-focus-ring-color}button,input,optgroup,select,textarea{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button,select{text-transform:none}[role=button]{cursor:pointer}select{word-wrap:normal}[type=button],[type=reset],[type=submit],button{-webkit-appearance:button}[type=button]:not(:disabled),[type=reset]:not(:disabled),[type=submit]:not(:disabled),button:not(:disabled){cursor:pointer}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{padding:0;border-style:none}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}textarea{overflow:auto;resize:vertical}fieldset{min-width:0;padding:0;margin:0;border:0}legend{display:block;width:100%;max-width:100%;padding:0;margin-bottom:.5rem;font-size:1.5rem;line-height:inherit;color:inherit;white-space:normal}@media (max-width:1200px){legend{font-size:calc(1.275rem + .3vw)}}progress{vertical-align:baseline}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{outline-offset:-2px;-webkit-appearance:none}[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}output{display:inline-block}summary{display:list-item;cursor:pointer}template{display:none}[hidden]{display:none!important}.navbar{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:.5rem 1rem}.navbar .container,.navbar .container-fluid,.navbar .container-lg,.navbar .container-md,.navbar .container-sm,.navbar .container-xl{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-brand{display:inline-block;padding-top:.3125rem;padding-bottom:.3125rem;margin-right:1rem;font-size:1.25rem;line-height:inherit;white-space:nowrap}.navbar-brand:focus,.navbar-brand:hover{text-decoration:none}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .nav-link{padding-right:0;padding-left:0}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-text{display:inline-block;padding-top:.5rem;padding-bottom:.5rem}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:.25rem .75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:.15rem}.navbar-toggler:focus,.navbar-toggler:hover{text-decoration:none}.navbar-toggler-icon{display:inline-block;width:1.5em;height:1.5em;vertical-align:middle;content:"";background:no-repeat center center;background-size:100% 100%}@media (max-width:575.98px){.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid,.navbar-expand-sm>.container-lg,.navbar-expand-sm>.container-md,.navbar-expand-sm>.container-sm,.navbar-expand-sm>.container-xl{padding-right:0;padding-left:0}}@media (min-width:576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid,.navbar-expand-sm>.container-lg,.navbar-expand-sm>.container-md,.navbar-expand-sm>.container-sm,.navbar-expand-sm>.container-xl{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}@media (max-width:767.98px){.navbar-expand-md>.container,.navbar-expand-md>.container-fluid,.navbar-expand-md>.container-lg,.navbar-expand-md>.container-md,.navbar-expand-md>.container-sm,.navbar-expand-md>.container-xl{padding-right:0;padding-left:0}}@media (min-width:768px){.navbar-expand-md{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-md .navbar-nav{flex-direction:row}.navbar-expand-md .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-md .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-md>.container,.navbar-expand-md>.container-fluid,.navbar-expand-md>.container-lg,.navbar-expand-md>.container-md,.navbar-expand-md>.container-sm,.navbar-expand-md>.container-xl{flex-wrap:nowrap}.navbar-expand-md .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-md .navbar-toggler{display:none}}@media (max-width:991.98px){.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid,.navbar-expand-lg>.container-lg,.navbar-expand-lg>.container-md,.navbar-expand-lg>.container-sm,.navbar-expand-lg>.container-xl{padding-right:0;padding-left:0}}@media (min-width:992px){.navbar-expand-lg{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-lg .navbar-nav{flex-direction:row}.navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-lg .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid,.navbar-expand-lg>.container-lg,.navbar-expand-lg>.container-md,.navbar-expand-lg>.container-sm,.navbar-expand-lg>.container-xl{flex-wrap:nowrap}.navbar-expand-lg .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-lg .navbar-toggler{display:none}}@media (max-width:1199.98px){.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid,.navbar-expand-xl>.container-lg,.navbar-expand-xl>.container-md,.navbar-expand-xl>.container-sm,.navbar-expand-xl>.container-xl{padding-right:0;padding-left:0}}@media (min-width:1200px){.navbar-expand-xl{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-xl .navbar-nav{flex-direction:row}.navbar-expand-xl .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-xl .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid,.navbar-expand-xl>.container-lg,.navbar-expand-xl>.container-md,.navbar-expand-xl>.container-sm,.navbar-expand-xl>.container-xl{flex-wrap:nowrap}.navbar-expand-xl .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-xl .navbar-toggler{display:none}}.navbar-expand{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand>.container,.navbar-expand>.container-fluid,.navbar-expand>.container-lg,.navbar-expand>.container-md,.navbar-expand>.container-sm,.navbar-expand>.container-xl{padding-right:0;padding-left:0}.navbar-expand .navbar-nav{flex-direction:row}.navbar-expand .navbar-nav .dropdown-menu{position:absolute}.navbar-expand .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand>.container,.navbar-expand>.container-fluid,.navbar-expand>.container-lg,.navbar-expand>.container-md,.navbar-expand>.container-sm,.navbar-expand>.container-xl{flex-wrap:nowrap}.navbar-expand .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand .navbar-toggler{display:none}.navbar-light .navbar-brand{color:rgba(0,0,0,.9)}.navbar-light .navbar-brand:focus,.navbar-light .navbar-brand:hover{color:rgba(0,0,0,.9)}.navbar-light .navbar-nav .nav-link{color:rgba(0,0,0,.5)}.navbar-light .navbar-nav .nav-link:focus,.navbar-light .navbar-nav .nav-link:hover{color:rgba(0,0,0,.7)}.navbar-light .navbar-nav .nav-link.disabled{color:rgba(0,0,0,.3)}.navbar-light .navbar-nav .active>.nav-link,.navbar-light .navbar-nav .nav-link.active,.navbar-light .navbar-nav .nav-link.show,.navbar-light .navbar-nav .show>.nav-link{color:rgba(0,0,0,.9)}.navbar-light .navbar-toggler{color:rgba(0,0,0,.5);border-color:rgba(0,0,0,.1)}.navbar-light .navbar-toggler-icon{background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%280, 0, 0, 0.5%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")}.navbar-light .navbar-text{color:rgba(0,0,0,.5)}.navbar-light .navbar-text a{color:rgba(0,0,0,.9)}.navbar-light .navbar-text a:focus,.navbar-light .navbar-text a:hover{color:rgba(0,0,0,.9)}.navbar-dark .navbar-brand{color:#fff}.navbar-dark .navbar-brand:focus,.navbar-dark .navbar-brand:hover{color:#fff}.navbar-dark .navbar-nav .nav-link{color:rgba(255,255,255,.5)}.navbar-dark .navbar-nav .nav-link:focus,.navbar-dark .navbar-nav .nav-link:hover{color:rgba(255,255,255,.75)}.navbar-dark .navbar-nav .nav-link.disabled{color:rgba(255,255,255,.25)}.navbar-dark .navbar-nav .active>.nav-link,.navbar-dark .navbar-nav .nav-link.active,.navbar-dark .navbar-nav .nav-link.show,.navbar-dark .navbar-nav .show>.nav-link{color:#fff}.navbar-dark .navbar-toggler{color:rgba(255,255,255,.5);border-color:rgba(255,255,255,.1)}.navbar-dark .navbar-toggler-icon{background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.5%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")}.navbar-dark .navbar-text{color:rgba(255,255,255,.5)}.navbar-dark .navbar-text a{color:#fff}.navbar-dark .navbar-text a:focus,.navbar-dark .navbar-text a:hover{color:#fff}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.nav-link{display:block;padding:.5rem 1rem}.nav-link:focus,.nav-link:hover{text-decoration:none}.nav-link.disabled{color:#6c757d;pointer-events:none;cursor:default}.nav-tabs{border-bottom:1px solid #dee2e6}.nav-tabs .nav-item{margin-bottom:-1px}.nav-tabs .nav-link{border:1px solid transparent;border-top-left-radius:.15rem;border-top-right-radius:.15rem}.nav-tabs .nav-link:focus,.nav-tabs .nav-link:hover{border-color:#e9ecef #e9ecef #dee2e6}.nav-tabs .nav-link.disabled{color:#6c757d;background-color:transparent;border-color:transparent}.nav-tabs .nav-item.show .nav-link,.nav-tabs .nav-link.active{color:#495057;background-color:#fff;border-color:#dee2e6 #dee2e6 #fff}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-left-radius:0;border-top-right-radius:0}.nav-pills .nav-link{border-radius:.15rem}.nav-pills .nav-link.active,.nav-pills .show>.nav-link{color:#fff;background-color:#1377c3}.nav-fill .nav-item{flex:1 1 auto;text-align:center}.nav-justified .nav-item{flex-basis:0;flex-grow:1;text-align:center}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.modal-open{overflow:hidden}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal{position:fixed;top:0;left:0;z-index:1050;display:none;width:100%;height:100%;overflow:hidden;outline:0}.modal-dialog{position:relative;width:auto;margin:.5rem;pointer-events:none}.modal.fade .modal-dialog{transition:transform .3s ease-out;transform:translate(0,-50px)}@media (prefers-reduced-motion:reduce){.modal.fade .modal-dialog{transition:none}}.modal.show .modal-dialog{transform:none}.modal.modal-static .modal-dialog{transform:scale(1.02)}.modal-dialog-scrollable{display:flex;max-height:calc(100% - 1rem)}.modal-dialog-scrollable .modal-content{max-height:calc(100vh - 1rem);overflow:hidden}.modal-dialog-scrollable .modal-footer,.modal-dialog-scrollable .modal-header{flex-shrink:0}.modal-dialog-scrollable .modal-body{overflow-y:auto}.modal-dialog-centered{display:flex;align-items:center;min-height:calc(100% - 1rem)}.modal-dialog-centered::before{display:block;height:calc(100vh - 1rem);height:-moz-min-content;height:min-content;content:""}.modal-dialog-centered.modal-dialog-scrollable{flex-direction:column;justify-content:center;height:100%}.modal-dialog-centered.modal-dialog-scrollable .modal-content{max-height:none}.modal-dialog-centered.modal-dialog-scrollable::before{content:none}.modal-content{position:relative;display:flex;flex-direction:column;width:100%;pointer-events:auto;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem;outline:0}.modal-backdrop{position:fixed;top:0;left:0;z-index:1040;width:100vw;height:100vh;background-color:#000}.modal-backdrop.fade{opacity:0}.modal-backdrop.show{opacity:.5}.modal-header{display:flex;align-items:flex-start;justify-content:space-between;padding:1rem 1rem;border-bottom:1px solid #e9ecef;border-top-left-radius:calc(.3rem - 1px);border-top-right-radius:calc(.3rem - 1px)}.modal-header .close{padding:1rem 1rem;margin:-1rem -1rem -1rem auto}.modal-title{margin-bottom:0;line-height:1.5}.modal-body{position:relative;flex:1 1 auto;padding:1rem}.modal-footer{display:flex;flex-wrap:wrap;align-items:center;justify-content:flex-end;padding:.75rem;border-top:1px solid #e9ecef;border-bottom-right-radius:calc(.3rem - 1px);border-bottom-left-radius:calc(.3rem - 1px)}.modal-footer>*{margin:.25rem}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:576px){.modal-dialog{max-width:500px;margin:1.75rem auto}.modal-dialog-scrollable{max-height:calc(100% - 3.5rem)}.modal-dialog-scrollable .modal-content{max-height:calc(100vh - 3.5rem)}.modal-dialog-centered{min-height:calc(100% - 3.5rem)}.modal-dialog-centered::before{height:calc(100vh - 3.5rem);height:-moz-min-content;height:min-content}.modal-sm{max-width:300px}}@media (min-width:992px){.modal-lg,.modal-xl{max-width:800px}}@media (min-width:1200px){.modal-xl{max-width:1140px}}.modal-fullw{max-width:95vw}.align-baseline{vertical-align:baseline!important}.align-top{vertical-align:top!important}.align-middle{vertical-align:middle!important}.align-bottom{vertical-align:bottom!important}.align-text-bottom{vertical-align:text-bottom!important}.align-text-top{vertical-align:text-top!important}.bg-primary{background-color:#1377c3!important}a.bg-primary:focus,a.bg-primary:hover,button.bg-primary:focus,button.bg-primary:hover{background-color:#0e5b95!important}.bg-primarystrong{background-color:#0c4c7d!important}a.bg-primarystrong:focus,a.bg-primarystrong:hover,button.bg-primarystrong:focus,button.bg-primarystrong:hover{background-color:#08304e!important}.bg-secondary{background-color:#677689!important}a.bg-secondary:focus,a.bg-secondary:hover,button.bg-secondary:focus,button.bg-secondary:hover{background-color:#515d6c!important}.bg-success{background-color:#218739!important}a.bg-success:focus,a.bg-success:hover,button.bg-success:focus,button.bg-success:hover{background-color:#175e28!important}.bg-info{background-color:#17a2b8!important}a.bg-info:focus,a.bg-info:hover,button.bg-info:focus,button.bg-info:hover{background-color:#117a8b!important}.bg-warning{background-color:#ffc107!important}a.bg-warning:focus,a.bg-warning:hover,button.bg-warning:focus,button.bg-warning:hover{background-color:#d39e00!important}.bg-danger{background-color:#dc3545!important}a.bg-danger:focus,a.bg-danger:hover,button.bg-danger:focus,button.bg-danger:hover{background-color:#bd2130!important}.bg-light{background-color:#f8f9fa!important}a.bg-light:focus,a.bg-light:hover,button.bg-light:focus,button.bg-light:hover{background-color:#dae0e5!important}.bg-dark{background-color:#343a40!important}a.bg-dark:focus,a.bg-dark:hover,button.bg-dark:focus,button.bg-dark:hover{background-color:#1d2124!important}.bg-accentprimary{background-color:#0e558b!important}a.bg-accentprimary:focus,a.bg-accentprimary:hover,button.bg-accentprimary:focus,button.bg-accentprimary:hover{background-color:#09395d!important}.bg-secondarylight{background-color:#6c727f!important}a.bg-secondarylight:focus,a.bg-secondarylight:hover,button.bg-secondarylight:focus,button.bg-secondarylight:hover{background-color:#555963!important}.bg-white{background-color:#fff!important}.bg-transparent{background-color:transparent!important}.border{border:1px solid #dee2e6!important}.border-top{border-top:1px solid #dee2e6!important}.border-right{border-right:1px solid #dee2e6!important}.border-bottom{border-bottom:1px solid #dee2e6!important}.border-left{border-left:1px solid #dee2e6!important}.border-0{border:0!important}.border-top-0{border-top:0!important}.border-right-0{border-right:0!important}.border-bottom-0{border-bottom:0!important}.border-left-0{border-left:0!important}.border-primary{border-color:#1377c3!important}.border-primarystrong{border-color:#0c4c7d!important}.border-secondary{border-color:#677689!important}.border-success{border-color:#218739!important}.border-info{border-color:#17a2b8!important}.border-warning{border-color:#ffc107!important}.border-danger{border-color:#dc3545!important}.border-light{border-color:#f8f9fa!important}.border-dark{border-color:#343a40!important}.border-accentprimary{border-color:#0e558b!important}.border-secondarylight{border-color:#6c727f!important}.border-white{border-color:#fff!important}.rounded-sm{border-radius:.2rem!important}.rounded{border-radius:.15rem!important}.rounded-top{border-top-left-radius:.15rem!important;border-top-right-radius:.15rem!important}.rounded-right{border-top-right-radius:.15rem!important;border-bottom-right-radius:.15rem!important}.rounded-bottom{border-bottom-right-radius:.15rem!important;border-bottom-left-radius:.15rem!important}.rounded-left{border-top-left-radius:.15rem!important;border-bottom-left-radius:.15rem!important}.rounded-lg{border-radius:.3rem!important}.rounded-circle{border-radius:50%!important}.rounded-pill{border-radius:50rem!important}.rounded-0{border-radius:0!important}.clearfix::after{display:block;clear:both;content:""}.d-none{display:none!important}.d-inline{display:inline!important}.d-inline-block{display:inline-block!important}.d-block{display:block!important}.d-table{display:table!important}.d-table-row{display:table-row!important}.d-table-cell{display:table-cell!important}.d-flex{display:flex!important}.d-inline-flex{display:inline-flex!important}@media (min-width:576px){.d-sm-none{display:none!important}.d-sm-inline{display:inline!important}.d-sm-inline-block{display:inline-block!important}.d-sm-block{display:block!important}.d-sm-table{display:table!important}.d-sm-table-row{display:table-row!important}.d-sm-table-cell{display:table-cell!important}.d-sm-flex{display:flex!important}.d-sm-inline-flex{display:inline-flex!important}}@media (min-width:768px){.d-md-none{display:none!important}.d-md-inline{display:inline!important}.d-md-inline-block{display:inline-block!important}.d-md-block{display:block!important}.d-md-table{display:table!important}.d-md-table-row{display:table-row!important}.d-md-table-cell{display:table-cell!important}.d-md-flex{display:flex!important}.d-md-inline-flex{display:inline-flex!important}}@media (min-width:992px){.d-lg-none{display:none!important}.d-lg-inline{display:inline!important}.d-lg-inline-block{display:inline-block!important}.d-lg-block{display:block!important}.d-lg-table{display:table!important}.d-lg-table-row{display:table-row!important}.d-lg-table-cell{display:table-cell!important}.d-lg-flex{display:flex!important}.d-lg-inline-flex{display:inline-flex!important}}@media (min-width:1200px){.d-xl-none{display:none!important}.d-xl-inline{display:inline!important}.d-xl-inline-block{display:inline-block!important}.d-xl-block{display:block!important}.d-xl-table{display:table!important}.d-xl-table-row{display:table-row!important}.d-xl-table-cell{display:table-cell!important}.d-xl-flex{display:flex!important}.d-xl-inline-flex{display:inline-flex!important}}@media print{.d-print-none{display:none!important}.d-print-inline{display:inline!important}.d-print-inline-block{display:inline-block!important}.d-print-block{display:block!important}.d-print-table{display:table!important}.d-print-table-row{display:table-row!important}.d-print-table-cell{display:table-cell!important}.d-print-flex{display:flex!important}.d-print-inline-flex{display:inline-flex!important}}.embed-responsive{position:relative;display:block;width:100%;padding:0;overflow:hidden}.embed-responsive::before{display:block;content:""}.embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;bottom:0;left:0;width:100%;height:100%;border:0}.embed-responsive-21by9::before{padding-top:42.8571428571%}.embed-responsive-16by9::before{padding-top:56.25%}.embed-responsive-4by3::before{padding-top:75%}.embed-responsive-1by1::before{padding-top:100%}.embed-responsive-21by9::before{padding-top:42.8571428571%}.embed-responsive-16by9::before{padding-top:56.25%}.embed-responsive-4by3::before{padding-top:75%}.embed-responsive-1by1::before{padding-top:100%}.flex-row{flex-direction:row!important}.flex-column{flex-direction:column!important}.flex-row-reverse{flex-direction:row-reverse!important}.flex-column-reverse{flex-direction:column-reverse!important}.flex-wrap{flex-wrap:wrap!important}.flex-nowrap{flex-wrap:nowrap!important}.flex-wrap-reverse{flex-wrap:wrap-reverse!important}.flex-fill{flex:1 1 auto!important}.flex-grow-0{flex-grow:0!important}.flex-grow-1{flex-grow:1!important}.flex-shrink-0{flex-shrink:0!important}.flex-shrink-1{flex-shrink:1!important}.justify-content-start{justify-content:flex-start!important}.justify-content-end{justify-content:flex-end!important}.justify-content-center{justify-content:center!important}.justify-content-between{justify-content:space-between!important}.justify-content-around{justify-content:space-around!important}.align-items-start{align-items:flex-start!important}.align-items-end{align-items:flex-end!important}.align-items-center{align-items:center!important}.align-items-baseline{align-items:baseline!important}.align-items-stretch{align-items:stretch!important}.align-content-start{align-content:flex-start!important}.align-content-end{align-content:flex-end!important}.align-content-center{align-content:center!important}.align-content-between{align-content:space-between!important}.align-content-around{align-content:space-around!important}.align-content-stretch{align-content:stretch!important}.align-self-auto{align-self:auto!important}.align-self-start{align-self:flex-start!important}.align-self-end{align-self:flex-end!important}.align-self-center{align-self:center!important}.align-self-baseline{align-self:baseline!important}.align-self-stretch{align-self:stretch!important}@media (min-width:576px){.flex-sm-row{flex-direction:row!important}.flex-sm-column{flex-direction:column!important}.flex-sm-row-reverse{flex-direction:row-reverse!important}.flex-sm-column-reverse{flex-direction:column-reverse!important}.flex-sm-wrap{flex-wrap:wrap!important}.flex-sm-nowrap{flex-wrap:nowrap!important}.flex-sm-wrap-reverse{flex-wrap:wrap-reverse!important}.flex-sm-fill{flex:1 1 auto!important}.flex-sm-grow-0{flex-grow:0!important}.flex-sm-grow-1{flex-grow:1!important}.flex-sm-shrink-0{flex-shrink:0!important}.flex-sm-shrink-1{flex-shrink:1!important}.justify-content-sm-start{justify-content:flex-start!important}.justify-content-sm-end{justify-content:flex-end!important}.justify-content-sm-center{justify-content:center!important}.justify-content-sm-between{justify-content:space-between!important}.justify-content-sm-around{justify-content:space-around!important}.align-items-sm-start{align-items:flex-start!important}.align-items-sm-end{align-items:flex-end!important}.align-items-sm-center{align-items:center!important}.align-items-sm-baseline{align-items:baseline!important}.align-items-sm-stretch{align-items:stretch!important}.align-content-sm-start{align-content:flex-start!important}.align-content-sm-end{align-content:flex-end!important}.align-content-sm-center{align-content:center!important}.align-content-sm-between{align-content:space-between!important}.align-content-sm-around{align-content:space-around!important}.align-content-sm-stretch{align-content:stretch!important}.align-self-sm-auto{align-self:auto!important}.align-self-sm-start{align-self:flex-start!important}.align-self-sm-end{align-self:flex-end!important}.align-self-sm-center{align-self:center!important}.align-self-sm-baseline{align-self:baseline!important}.align-self-sm-stretch{align-self:stretch!important}}@media (min-width:768px){.flex-md-row{flex-direction:row!important}.flex-md-column{flex-direction:column!important}.flex-md-row-reverse{flex-direction:row-reverse!important}.flex-md-column-reverse{flex-direction:column-reverse!important}.flex-md-wrap{flex-wrap:wrap!important}.flex-md-nowrap{flex-wrap:nowrap!important}.flex-md-wrap-reverse{flex-wrap:wrap-reverse!important}.flex-md-fill{flex:1 1 auto!important}.flex-md-grow-0{flex-grow:0!important}.flex-md-grow-1{flex-grow:1!important}.flex-md-shrink-0{flex-shrink:0!important}.flex-md-shrink-1{flex-shrink:1!important}.justify-content-md-start{justify-content:flex-start!important}.justify-content-md-end{justify-content:flex-end!important}.justify-content-md-center{justify-content:center!important}.justify-content-md-between{justify-content:space-between!important}.justify-content-md-around{justify-content:space-around!important}.align-items-md-start{align-items:flex-start!important}.align-items-md-end{align-items:flex-end!important}.align-items-md-center{align-items:center!important}.align-items-md-baseline{align-items:baseline!important}.align-items-md-stretch{align-items:stretch!important}.align-content-md-start{align-content:flex-start!important}.align-content-md-end{align-content:flex-end!important}.align-content-md-center{align-content:center!important}.align-content-md-between{align-content:space-between!important}.align-content-md-around{align-content:space-around!important}.align-content-md-stretch{align-content:stretch!important}.align-self-md-auto{align-self:auto!important}.align-self-md-start{align-self:flex-start!important}.align-self-md-end{align-self:flex-end!important}.align-self-md-center{align-self:center!important}.align-self-md-baseline{align-self:baseline!important}.align-self-md-stretch{align-self:stretch!important}}@media (min-width:992px){.flex-lg-row{flex-direction:row!important}.flex-lg-column{flex-direction:column!important}.flex-lg-row-reverse{flex-direction:row-reverse!important}.flex-lg-column-reverse{flex-direction:column-reverse!important}.flex-lg-wrap{flex-wrap:wrap!important}.flex-lg-nowrap{flex-wrap:nowrap!important}.flex-lg-wrap-reverse{flex-wrap:wrap-reverse!important}.flex-lg-fill{flex:1 1 auto!important}.flex-lg-grow-0{flex-grow:0!important}.flex-lg-grow-1{flex-grow:1!important}.flex-lg-shrink-0{flex-shrink:0!important}.flex-lg-shrink-1{flex-shrink:1!important}.justify-content-lg-start{justify-content:flex-start!important}.justify-content-lg-end{justify-content:flex-end!important}.justify-content-lg-center{justify-content:center!important}.justify-content-lg-between{justify-content:space-between!important}.justify-content-lg-around{justify-content:space-around!important}.align-items-lg-start{align-items:flex-start!important}.align-items-lg-end{align-items:flex-end!important}.align-items-lg-center{align-items:center!important}.align-items-lg-baseline{align-items:baseline!important}.align-items-lg-stretch{align-items:stretch!important}.align-content-lg-start{align-content:flex-start!important}.align-content-lg-end{align-content:flex-end!important}.align-content-lg-center{align-content:center!important}.align-content-lg-between{align-content:space-between!important}.align-content-lg-around{align-content:space-around!important}.align-content-lg-stretch{align-content:stretch!important}.align-self-lg-auto{align-self:auto!important}.align-self-lg-start{align-self:flex-start!important}.align-self-lg-end{align-self:flex-end!important}.align-self-lg-center{align-self:center!important}.align-self-lg-baseline{align-self:baseline!important}.align-self-lg-stretch{align-self:stretch!important}}@media (min-width:1200px){.flex-xl-row{flex-direction:row!important}.flex-xl-column{flex-direction:column!important}.flex-xl-row-reverse{flex-direction:row-reverse!important}.flex-xl-column-reverse{flex-direction:column-reverse!important}.flex-xl-wrap{flex-wrap:wrap!important}.flex-xl-nowrap{flex-wrap:nowrap!important}.flex-xl-wrap-reverse{flex-wrap:wrap-reverse!important}.flex-xl-fill{flex:1 1 auto!important}.flex-xl-grow-0{flex-grow:0!important}.flex-xl-grow-1{flex-grow:1!important}.flex-xl-shrink-0{flex-shrink:0!important}.flex-xl-shrink-1{flex-shrink:1!important}.justify-content-xl-start{justify-content:flex-start!important}.justify-content-xl-end{justify-content:flex-end!important}.justify-content-xl-center{justify-content:center!important}.justify-content-xl-between{justify-content:space-between!important}.justify-content-xl-around{justify-content:space-around!important}.align-items-xl-start{align-items:flex-start!important}.align-items-xl-end{align-items:flex-end!important}.align-items-xl-center{align-items:center!important}.align-items-xl-baseline{align-items:baseline!important}.align-items-xl-stretch{align-items:stretch!important}.align-content-xl-start{align-content:flex-start!important}.align-content-xl-end{align-content:flex-end!important}.align-content-xl-center{align-content:center!important}.align-content-xl-between{align-content:space-between!important}.align-content-xl-around{align-content:space-around!important}.align-content-xl-stretch{align-content:stretch!important}.align-self-xl-auto{align-self:auto!important}.align-self-xl-start{align-self:flex-start!important}.align-self-xl-end{align-self:flex-end!important}.align-self-xl-center{align-self:center!important}.align-self-xl-baseline{align-self:baseline!important}.align-self-xl-stretch{align-self:stretch!important}}.float-left{float:left!important}.float-right{float:right!important}.float-none{float:none!important}@media (min-width:576px){.float-sm-left{float:left!important}.float-sm-right{float:right!important}.float-sm-none{float:none!important}}@media (min-width:768px){.float-md-left{float:left!important}.float-md-right{float:right!important}.float-md-none{float:none!important}}@media (min-width:992px){.float-lg-left{float:left!important}.float-lg-right{float:right!important}.float-lg-none{float:none!important}}@media (min-width:1200px){.float-xl-left{float:left!important}.float-xl-right{float:right!important}.float-xl-none{float:none!important}}.user-select-all{-webkit-user-select:all!important;-moz-user-select:all!important;user-select:all!important}.user-select-auto{-webkit-user-select:auto!important;-moz-user-select:auto!important;user-select:auto!important}.user-select-none{-webkit-user-select:none!important;-moz-user-select:none!important;user-select:none!important}.overflow-auto{overflow:auto!important}.overflow-hidden{overflow:hidden!important}.position-static{position:static!important}.position-relative{position:relative!important}.position-absolute{position:absolute!important}.position-fixed{position:fixed!important}.position-sticky{position:sticky!important}.fixed-top{position:fixed;top:0;right:0;left:0;z-index:1030}.fixed-bottom{position:fixed;right:0;bottom:0;left:0;z-index:1030}@supports (position:sticky){.sticky-top{position:sticky;top:0;z-index:1020}}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;overflow:visible;clip:auto;white-space:normal}.shadow-sm{box-shadow:0 .125rem .25rem rgba(0,0,0,.075)!important}.shadow{box-shadow:0 .5rem 1rem rgba(0,0,0,.15)!important}.shadow-lg{box-shadow:0 1rem 3rem rgba(0,0,0,.175)!important}.shadow-none{box-shadow:none!important}.w-25{width:25%!important}.w-50{width:50%!important}.w-75{width:75%!important}.w-100{width:100%!important}.w-auto{width:auto!important}.h-25{height:25%!important}.h-50{height:50%!important}.h-75{height:75%!important}.h-100{height:100%!important}.h-auto{height:auto!important}.mw-100{max-width:100%!important}.mh-100{max-height:100%!important}.min-vw-100{min-width:100vw!important}.min-vh-100{min-height:100vh!important}.vw-100{width:100vw!important}.vh-100{height:100vh!important}.m-0{margin:0!important}.mt-0,.my-0{margin-top:0!important}.mr-0,.mx-0{margin-right:0!important}.mb-0,.my-0{margin-bottom:0!important}.ml-0,.mx-0{margin-left:0!important}.m-1{margin:.25rem!important}.mt-1,.my-1{margin-top:.25rem!important}.mr-1,.mx-1{margin-right:.25rem!important}.mb-1,.my-1{margin-bottom:.25rem!important}.ml-1,.mx-1{margin-left:.25rem!important}.m-2{margin:.5rem!important}.mt-2,.my-2{margin-top:.5rem!important}.mr-2,.mx-2{margin-right:.5rem!important}.mb-2,.my-2{margin-bottom:.5rem!important}.ml-2,.mx-2{margin-left:.5rem!important}.m-3{margin:1rem!important}.mt-3,.my-3{margin-top:1rem!important}.mr-3,.mx-3{margin-right:1rem!important}.mb-3,.my-3{margin-bottom:1rem!important}.ml-3,.mx-3{margin-left:1rem!important}.m-4{margin:1.5rem!important}.mt-4,.my-4{margin-top:1.5rem!important}.mr-4,.mx-4{margin-right:1.5rem!important}.mb-4,.my-4{margin-bottom:1.5rem!important}.ml-4,.mx-4{margin-left:1.5rem!important}.m-5{margin:3rem!important}.mt-5,.my-5{margin-top:3rem!important}.mr-5,.mx-5{margin-right:3rem!important}.mb-5,.my-5{margin-bottom:3rem!important}.ml-5,.mx-5{margin-left:3rem!important}.m-6{margin:4rem!important}.mt-6,.my-6{margin-top:4rem!important}.mr-6,.mx-6{margin-right:4rem!important}.mb-6,.my-6{margin-bottom:4rem!important}.ml-6,.mx-6{margin-left:4rem!important}.p-0{padding:0!important}.pt-0,.py-0{padding-top:0!important}.pr-0,.px-0{padding-right:0!important}.pb-0,.py-0{padding-bottom:0!important}.pl-0,.px-0{padding-left:0!important}.p-1{padding:.25rem!important}.pt-1,.py-1{padding-top:.25rem!important}.pr-1,.px-1{padding-right:.25rem!important}.pb-1,.py-1{padding-bottom:.25rem!important}.pl-1,.px-1{padding-left:.25rem!important}.p-2{padding:.5rem!important}.pt-2,.py-2{padding-top:.5rem!important}.pr-2,.px-2{padding-right:.5rem!important}.pb-2,.py-2{padding-bottom:.5rem!important}.pl-2,.px-2{padding-left:.5rem!important}.p-3{padding:1rem!important}.pt-3,.py-3{padding-top:1rem!important}.pr-3,.px-3{padding-right:1rem!important}.pb-3,.py-3{padding-bottom:1rem!important}.pl-3,.px-3{padding-left:1rem!important}.p-4{padding:1.5rem!important}.pt-4,.py-4{padding-top:1.5rem!important}.pr-4,.px-4{padding-right:1.5rem!important}.pb-4,.py-4{padding-bottom:1.5rem!important}.pl-4,.px-4{padding-left:1.5rem!important}.p-5{padding:3rem!important}.pt-5,.py-5{padding-top:3rem!important}.pr-5,.px-5{padding-right:3rem!important}.pb-5,.py-5{padding-bottom:3rem!important}.pl-5,.px-5{padding-left:3rem!important}.p-6{padding:4rem!important}.pt-6,.py-6{padding-top:4rem!important}.pr-6,.px-6{padding-right:4rem!important}.pb-6,.py-6{padding-bottom:4rem!important}.pl-6,.px-6{padding-left:4rem!important}.m-n1{margin:-.25rem!important}.mt-n1,.my-n1{margin-top:-.25rem!important}.mr-n1,.mx-n1{margin-right:-.25rem!important}.mb-n1,.my-n1{margin-bottom:-.25rem!important}.ml-n1,.mx-n1{margin-left:-.25rem!important}.m-n2{margin:-.5rem!important}.mt-n2,.my-n2{margin-top:-.5rem!important}.mr-n2,.mx-n2{margin-right:-.5rem!important}.mb-n2,.my-n2{margin-bottom:-.5rem!important}.ml-n2,.mx-n2{margin-left:-.5rem!important}.m-n3{margin:-1rem!important}.mt-n3,.my-n3{margin-top:-1rem!important}.mr-n3,.mx-n3{margin-right:-1rem!important}.mb-n3,.my-n3{margin-bottom:-1rem!important}.ml-n3,.mx-n3{margin-left:-1rem!important}.m-n4{margin:-1.5rem!important}.mt-n4,.my-n4{margin-top:-1.5rem!important}.mr-n4,.mx-n4{margin-right:-1.5rem!important}.mb-n4,.my-n4{margin-bottom:-1.5rem!important}.ml-n4,.mx-n4{margin-left:-1.5rem!important}.m-n5{margin:-3rem!important}.mt-n5,.my-n5{margin-top:-3rem!important}.mr-n5,.mx-n5{margin-right:-3rem!important}.mb-n5,.my-n5{margin-bottom:-3rem!important}.ml-n5,.mx-n5{margin-left:-3rem!important}.m-n6{margin:-4rem!important}.mt-n6,.my-n6{margin-top:-4rem!important}.mr-n6,.mx-n6{margin-right:-4rem!important}.mb-n6,.my-n6{margin-bottom:-4rem!important}.ml-n6,.mx-n6{margin-left:-4rem!important}.m-auto{margin:auto!important}.mt-auto,.my-auto{margin-top:auto!important}.mr-auto,.mx-auto{margin-right:auto!important}.mb-auto,.my-auto{margin-bottom:auto!important}.ml-auto,.mx-auto{margin-left:auto!important}@media (min-width:576px){.m-sm-0{margin:0!important}.mt-sm-0,.my-sm-0{margin-top:0!important}.mr-sm-0,.mx-sm-0{margin-right:0!important}.mb-sm-0,.my-sm-0{margin-bottom:0!important}.ml-sm-0,.mx-sm-0{margin-left:0!important}.m-sm-1{margin:.25rem!important}.mt-sm-1,.my-sm-1{margin-top:.25rem!important}.mr-sm-1,.mx-sm-1{margin-right:.25rem!important}.mb-sm-1,.my-sm-1{margin-bottom:.25rem!important}.ml-sm-1,.mx-sm-1{margin-left:.25rem!important}.m-sm-2{margin:.5rem!important}.mt-sm-2,.my-sm-2{margin-top:.5rem!important}.mr-sm-2,.mx-sm-2{margin-right:.5rem!important}.mb-sm-2,.my-sm-2{margin-bottom:.5rem!important}.ml-sm-2,.mx-sm-2{margin-left:.5rem!important}.m-sm-3{margin:1rem!important}.mt-sm-3,.my-sm-3{margin-top:1rem!important}.mr-sm-3,.mx-sm-3{margin-right:1rem!important}.mb-sm-3,.my-sm-3{margin-bottom:1rem!important}.ml-sm-3,.mx-sm-3{margin-left:1rem!important}.m-sm-4{margin:1.5rem!important}.mt-sm-4,.my-sm-4{margin-top:1.5rem!important}.mr-sm-4,.mx-sm-4{margin-right:1.5rem!important}.mb-sm-4,.my-sm-4{margin-bottom:1.5rem!important}.ml-sm-4,.mx-sm-4{margin-left:1.5rem!important}.m-sm-5{margin:3rem!important}.mt-sm-5,.my-sm-5{margin-top:3rem!important}.mr-sm-5,.mx-sm-5{margin-right:3rem!important}.mb-sm-5,.my-sm-5{margin-bottom:3rem!important}.ml-sm-5,.mx-sm-5{margin-left:3rem!important}.m-sm-6{margin:4rem!important}.mt-sm-6,.my-sm-6{margin-top:4rem!important}.mr-sm-6,.mx-sm-6{margin-right:4rem!important}.mb-sm-6,.my-sm-6{margin-bottom:4rem!important}.ml-sm-6,.mx-sm-6{margin-left:4rem!important}.p-sm-0{padding:0!important}.pt-sm-0,.py-sm-0{padding-top:0!important}.pr-sm-0,.px-sm-0{padding-right:0!important}.pb-sm-0,.py-sm-0{padding-bottom:0!important}.pl-sm-0,.px-sm-0{padding-left:0!important}.p-sm-1{padding:.25rem!important}.pt-sm-1,.py-sm-1{padding-top:.25rem!important}.pr-sm-1,.px-sm-1{padding-right:.25rem!important}.pb-sm-1,.py-sm-1{padding-bottom:.25rem!important}.pl-sm-1,.px-sm-1{padding-left:.25rem!important}.p-sm-2{padding:.5rem!important}.pt-sm-2,.py-sm-2{padding-top:.5rem!important}.pr-sm-2,.px-sm-2{padding-right:.5rem!important}.pb-sm-2,.py-sm-2{padding-bottom:.5rem!important}.pl-sm-2,.px-sm-2{padding-left:.5rem!important}.p-sm-3{padding:1rem!important}.pt-sm-3,.py-sm-3{padding-top:1rem!important}.pr-sm-3,.px-sm-3{padding-right:1rem!important}.pb-sm-3,.py-sm-3{padding-bottom:1rem!important}.pl-sm-3,.px-sm-3{padding-left:1rem!important}.p-sm-4{padding:1.5rem!important}.pt-sm-4,.py-sm-4{padding-top:1.5rem!important}.pr-sm-4,.px-sm-4{padding-right:1.5rem!important}.pb-sm-4,.py-sm-4{padding-bottom:1.5rem!important}.pl-sm-4,.px-sm-4{padding-left:1.5rem!important}.p-sm-5{padding:3rem!important}.pt-sm-5,.py-sm-5{padding-top:3rem!important}.pr-sm-5,.px-sm-5{padding-right:3rem!important}.pb-sm-5,.py-sm-5{padding-bottom:3rem!important}.pl-sm-5,.px-sm-5{padding-left:3rem!important}.p-sm-6{padding:4rem!important}.pt-sm-6,.py-sm-6{padding-top:4rem!important}.pr-sm-6,.px-sm-6{padding-right:4rem!important}.pb-sm-6,.py-sm-6{padding-bottom:4rem!important}.pl-sm-6,.px-sm-6{padding-left:4rem!important}.m-sm-n1{margin:-.25rem!important}.mt-sm-n1,.my-sm-n1{margin-top:-.25rem!important}.mr-sm-n1,.mx-sm-n1{margin-right:-.25rem!important}.mb-sm-n1,.my-sm-n1{margin-bottom:-.25rem!important}.ml-sm-n1,.mx-sm-n1{margin-left:-.25rem!important}.m-sm-n2{margin:-.5rem!important}.mt-sm-n2,.my-sm-n2{margin-top:-.5rem!important}.mr-sm-n2,.mx-sm-n2{margin-right:-.5rem!important}.mb-sm-n2,.my-sm-n2{margin-bottom:-.5rem!important}.ml-sm-n2,.mx-sm-n2{margin-left:-.5rem!important}.m-sm-n3{margin:-1rem!important}.mt-sm-n3,.my-sm-n3{margin-top:-1rem!important}.mr-sm-n3,.mx-sm-n3{margin-right:-1rem!important}.mb-sm-n3,.my-sm-n3{margin-bottom:-1rem!important}.ml-sm-n3,.mx-sm-n3{margin-left:-1rem!important}.m-sm-n4{margin:-1.5rem!important}.mt-sm-n4,.my-sm-n4{margin-top:-1.5rem!important}.mr-sm-n4,.mx-sm-n4{margin-right:-1.5rem!important}.mb-sm-n4,.my-sm-n4{margin-bottom:-1.5rem!important}.ml-sm-n4,.mx-sm-n4{margin-left:-1.5rem!important}.m-sm-n5{margin:-3rem!important}.mt-sm-n5,.my-sm-n5{margin-top:-3rem!important}.mr-sm-n5,.mx-sm-n5{margin-right:-3rem!important}.mb-sm-n5,.my-sm-n5{margin-bottom:-3rem!important}.ml-sm-n5,.mx-sm-n5{margin-left:-3rem!important}.m-sm-n6{margin:-4rem!important}.mt-sm-n6,.my-sm-n6{margin-top:-4rem!important}.mr-sm-n6,.mx-sm-n6{margin-right:-4rem!important}.mb-sm-n6,.my-sm-n6{margin-bottom:-4rem!important}.ml-sm-n6,.mx-sm-n6{margin-left:-4rem!important}.m-sm-auto{margin:auto!important}.mt-sm-auto,.my-sm-auto{margin-top:auto!important}.mr-sm-auto,.mx-sm-auto{margin-right:auto!important}.mb-sm-auto,.my-sm-auto{margin-bottom:auto!important}.ml-sm-auto,.mx-sm-auto{margin-left:auto!important}}@media (min-width:768px){.m-md-0{margin:0!important}.mt-md-0,.my-md-0{margin-top:0!important}.mr-md-0,.mx-md-0{margin-right:0!important}.mb-md-0,.my-md-0{margin-bottom:0!important}.ml-md-0,.mx-md-0{margin-left:0!important}.m-md-1{margin:.25rem!important}.mt-md-1,.my-md-1{margin-top:.25rem!important}.mr-md-1,.mx-md-1{margin-right:.25rem!important}.mb-md-1,.my-md-1{margin-bottom:.25rem!important}.ml-md-1,.mx-md-1{margin-left:.25rem!important}.m-md-2{margin:.5rem!important}.mt-md-2,.my-md-2{margin-top:.5rem!important}.mr-md-2,.mx-md-2{margin-right:.5rem!important}.mb-md-2,.my-md-2{margin-bottom:.5rem!important}.ml-md-2,.mx-md-2{margin-left:.5rem!important}.m-md-3{margin:1rem!important}.mt-md-3,.my-md-3{margin-top:1rem!important}.mr-md-3,.mx-md-3{margin-right:1rem!important}.mb-md-3,.my-md-3{margin-bottom:1rem!important}.ml-md-3,.mx-md-3{margin-left:1rem!important}.m-md-4{margin:1.5rem!important}.mt-md-4,.my-md-4{margin-top:1.5rem!important}.mr-md-4,.mx-md-4{margin-right:1.5rem!important}.mb-md-4,.my-md-4{margin-bottom:1.5rem!important}.ml-md-4,.mx-md-4{margin-left:1.5rem!important}.m-md-5{margin:3rem!important}.mt-md-5,.my-md-5{margin-top:3rem!important}.mr-md-5,.mx-md-5{margin-right:3rem!important}.mb-md-5,.my-md-5{margin-bottom:3rem!important}.ml-md-5,.mx-md-5{margin-left:3rem!important}.m-md-6{margin:4rem!important}.mt-md-6,.my-md-6{margin-top:4rem!important}.mr-md-6,.mx-md-6{margin-right:4rem!important}.mb-md-6,.my-md-6{margin-bottom:4rem!important}.ml-md-6,.mx-md-6{margin-left:4rem!important}.p-md-0{padding:0!important}.pt-md-0,.py-md-0{padding-top:0!important}.pr-md-0,.px-md-0{padding-right:0!important}.pb-md-0,.py-md-0{padding-bottom:0!important}.pl-md-0,.px-md-0{padding-left:0!important}.p-md-1{padding:.25rem!important}.pt-md-1,.py-md-1{padding-top:.25rem!important}.pr-md-1,.px-md-1{padding-right:.25rem!important}.pb-md-1,.py-md-1{padding-bottom:.25rem!important}.pl-md-1,.px-md-1{padding-left:.25rem!important}.p-md-2{padding:.5rem!important}.pt-md-2,.py-md-2{padding-top:.5rem!important}.pr-md-2,.px-md-2{padding-right:.5rem!important}.pb-md-2,.py-md-2{padding-bottom:.5rem!important}.pl-md-2,.px-md-2{padding-left:.5rem!important}.p-md-3{padding:1rem!important}.pt-md-3,.py-md-3{padding-top:1rem!important}.pr-md-3,.px-md-3{padding-right:1rem!important}.pb-md-3,.py-md-3{padding-bottom:1rem!important}.pl-md-3,.px-md-3{padding-left:1rem!important}.p-md-4{padding:1.5rem!important}.pt-md-4,.py-md-4{padding-top:1.5rem!important}.pr-md-4,.px-md-4{padding-right:1.5rem!important}.pb-md-4,.py-md-4{padding-bottom:1.5rem!important}.pl-md-4,.px-md-4{padding-left:1.5rem!important}.p-md-5{padding:3rem!important}.pt-md-5,.py-md-5{padding-top:3rem!important}.pr-md-5,.px-md-5{padding-right:3rem!important}.pb-md-5,.py-md-5{padding-bottom:3rem!important}.pl-md-5,.px-md-5{padding-left:3rem!important}.p-md-6{padding:4rem!important}.pt-md-6,.py-md-6{padding-top:4rem!important}.pr-md-6,.px-md-6{padding-right:4rem!important}.pb-md-6,.py-md-6{padding-bottom:4rem!important}.pl-md-6,.px-md-6{padding-left:4rem!important}.m-md-n1{margin:-.25rem!important}.mt-md-n1,.my-md-n1{margin-top:-.25rem!important}.mr-md-n1,.mx-md-n1{margin-right:-.25rem!important}.mb-md-n1,.my-md-n1{margin-bottom:-.25rem!important}.ml-md-n1,.mx-md-n1{margin-left:-.25rem!important}.m-md-n2{margin:-.5rem!important}.mt-md-n2,.my-md-n2{margin-top:-.5rem!important}.mr-md-n2,.mx-md-n2{margin-right:-.5rem!important}.mb-md-n2,.my-md-n2{margin-bottom:-.5rem!important}.ml-md-n2,.mx-md-n2{margin-left:-.5rem!important}.m-md-n3{margin:-1rem!important}.mt-md-n3,.my-md-n3{margin-top:-1rem!important}.mr-md-n3,.mx-md-n3{margin-right:-1rem!important}.mb-md-n3,.my-md-n3{margin-bottom:-1rem!important}.ml-md-n3,.mx-md-n3{margin-left:-1rem!important}.m-md-n4{margin:-1.5rem!important}.mt-md-n4,.my-md-n4{margin-top:-1.5rem!important}.mr-md-n4,.mx-md-n4{margin-right:-1.5rem!important}.mb-md-n4,.my-md-n4{margin-bottom:-1.5rem!important}.ml-md-n4,.mx-md-n4{margin-left:-1.5rem!important}.m-md-n5{margin:-3rem!important}.mt-md-n5,.my-md-n5{margin-top:-3rem!important}.mr-md-n5,.mx-md-n5{margin-right:-3rem!important}.mb-md-n5,.my-md-n5{margin-bottom:-3rem!important}.ml-md-n5,.mx-md-n5{margin-left:-3rem!important}.m-md-n6{margin:-4rem!important}.mt-md-n6,.my-md-n6{margin-top:-4rem!important}.mr-md-n6,.mx-md-n6{margin-right:-4rem!important}.mb-md-n6,.my-md-n6{margin-bottom:-4rem!important}.ml-md-n6,.mx-md-n6{margin-left:-4rem!important}.m-md-auto{margin:auto!important}.mt-md-auto,.my-md-auto{margin-top:auto!important}.mr-md-auto,.mx-md-auto{margin-right:auto!important}.mb-md-auto,.my-md-auto{margin-bottom:auto!important}.ml-md-auto,.mx-md-auto{margin-left:auto!important}}@media (min-width:992px){.m-lg-0{margin:0!important}.mt-lg-0,.my-lg-0{margin-top:0!important}.mr-lg-0,.mx-lg-0{margin-right:0!important}.mb-lg-0,.my-lg-0{margin-bottom:0!important}.ml-lg-0,.mx-lg-0{margin-left:0!important}.m-lg-1{margin:.25rem!important}.mt-lg-1,.my-lg-1{margin-top:.25rem!important}.mr-lg-1,.mx-lg-1{margin-right:.25rem!important}.mb-lg-1,.my-lg-1{margin-bottom:.25rem!important}.ml-lg-1,.mx-lg-1{margin-left:.25rem!important}.m-lg-2{margin:.5rem!important}.mt-lg-2,.my-lg-2{margin-top:.5rem!important}.mr-lg-2,.mx-lg-2{margin-right:.5rem!important}.mb-lg-2,.my-lg-2{margin-bottom:.5rem!important}.ml-lg-2,.mx-lg-2{margin-left:.5rem!important}.m-lg-3{margin:1rem!important}.mt-lg-3,.my-lg-3{margin-top:1rem!important}.mr-lg-3,.mx-lg-3{margin-right:1rem!important}.mb-lg-3,.my-lg-3{margin-bottom:1rem!important}.ml-lg-3,.mx-lg-3{margin-left:1rem!important}.m-lg-4{margin:1.5rem!important}.mt-lg-4,.my-lg-4{margin-top:1.5rem!important}.mr-lg-4,.mx-lg-4{margin-right:1.5rem!important}.mb-lg-4,.my-lg-4{margin-bottom:1.5rem!important}.ml-lg-4,.mx-lg-4{margin-left:1.5rem!important}.m-lg-5{margin:3rem!important}.mt-lg-5,.my-lg-5{margin-top:3rem!important}.mr-lg-5,.mx-lg-5{margin-right:3rem!important}.mb-lg-5,.my-lg-5{margin-bottom:3rem!important}.ml-lg-5,.mx-lg-5{margin-left:3rem!important}.m-lg-6{margin:4rem!important}.mt-lg-6,.my-lg-6{margin-top:4rem!important}.mr-lg-6,.mx-lg-6{margin-right:4rem!important}.mb-lg-6,.my-lg-6{margin-bottom:4rem!important}.ml-lg-6,.mx-lg-6{margin-left:4rem!important}.p-lg-0{padding:0!important}.pt-lg-0,.py-lg-0{padding-top:0!important}.pr-lg-0,.px-lg-0{padding-right:0!important}.pb-lg-0,.py-lg-0{padding-bottom:0!important}.pl-lg-0,.px-lg-0{padding-left:0!important}.p-lg-1{padding:.25rem!important}.pt-lg-1,.py-lg-1{padding-top:.25rem!important}.pr-lg-1,.px-lg-1{padding-right:.25rem!important}.pb-lg-1,.py-lg-1{padding-bottom:.25rem!important}.pl-lg-1,.px-lg-1{padding-left:.25rem!important}.p-lg-2{padding:.5rem!important}.pt-lg-2,.py-lg-2{padding-top:.5rem!important}.pr-lg-2,.px-lg-2{padding-right:.5rem!important}.pb-lg-2,.py-lg-2{padding-bottom:.5rem!important}.pl-lg-2,.px-lg-2{padding-left:.5rem!important}.p-lg-3{padding:1rem!important}.pt-lg-3,.py-lg-3{padding-top:1rem!important}.pr-lg-3,.px-lg-3{padding-right:1rem!important}.pb-lg-3,.py-lg-3{padding-bottom:1rem!important}.pl-lg-3,.px-lg-3{padding-left:1rem!important}.p-lg-4{padding:1.5rem!important}.pt-lg-4,.py-lg-4{padding-top:1.5rem!important}.pr-lg-4,.px-lg-4{padding-right:1.5rem!important}.pb-lg-4,.py-lg-4{padding-bottom:1.5rem!important}.pl-lg-4,.px-lg-4{padding-left:1.5rem!important}.p-lg-5{padding:3rem!important}.pt-lg-5,.py-lg-5{padding-top:3rem!important}.pr-lg-5,.px-lg-5{padding-right:3rem!important}.pb-lg-5,.py-lg-5{padding-bottom:3rem!important}.pl-lg-5,.px-lg-5{padding-left:3rem!important}.p-lg-6{padding:4rem!important}.pt-lg-6,.py-lg-6{padding-top:4rem!important}.pr-lg-6,.px-lg-6{padding-right:4rem!important}.pb-lg-6,.py-lg-6{padding-bottom:4rem!important}.pl-lg-6,.px-lg-6{padding-left:4rem!important}.m-lg-n1{margin:-.25rem!important}.mt-lg-n1,.my-lg-n1{margin-top:-.25rem!important}.mr-lg-n1,.mx-lg-n1{margin-right:-.25rem!important}.mb-lg-n1,.my-lg-n1{margin-bottom:-.25rem!important}.ml-lg-n1,.mx-lg-n1{margin-left:-.25rem!important}.m-lg-n2{margin:-.5rem!important}.mt-lg-n2,.my-lg-n2{margin-top:-.5rem!important}.mr-lg-n2,.mx-lg-n2{margin-right:-.5rem!important}.mb-lg-n2,.my-lg-n2{margin-bottom:-.5rem!important}.ml-lg-n2,.mx-lg-n2{margin-left:-.5rem!important}.m-lg-n3{margin:-1rem!important}.mt-lg-n3,.my-lg-n3{margin-top:-1rem!important}.mr-lg-n3,.mx-lg-n3{margin-right:-1rem!important}.mb-lg-n3,.my-lg-n3{margin-bottom:-1rem!important}.ml-lg-n3,.mx-lg-n3{margin-left:-1rem!important}.m-lg-n4{margin:-1.5rem!important}.mt-lg-n4,.my-lg-n4{margin-top:-1.5rem!important}.mr-lg-n4,.mx-lg-n4{margin-right:-1.5rem!important}.mb-lg-n4,.my-lg-n4{margin-bottom:-1.5rem!important}.ml-lg-n4,.mx-lg-n4{margin-left:-1.5rem!important}.m-lg-n5{margin:-3rem!important}.mt-lg-n5,.my-lg-n5{margin-top:-3rem!important}.mr-lg-n5,.mx-lg-n5{margin-right:-3rem!important}.mb-lg-n5,.my-lg-n5{margin-bottom:-3rem!important}.ml-lg-n5,.mx-lg-n5{margin-left:-3rem!important}.m-lg-n6{margin:-4rem!important}.mt-lg-n6,.my-lg-n6{margin-top:-4rem!important}.mr-lg-n6,.mx-lg-n6{margin-right:-4rem!important}.mb-lg-n6,.my-lg-n6{margin-bottom:-4rem!important}.ml-lg-n6,.mx-lg-n6{margin-left:-4rem!important}.m-lg-auto{margin:auto!important}.mt-lg-auto,.my-lg-auto{margin-top:auto!important}.mr-lg-auto,.mx-lg-auto{margin-right:auto!important}.mb-lg-auto,.my-lg-auto{margin-bottom:auto!important}.ml-lg-auto,.mx-lg-auto{margin-left:auto!important}}@media (min-width:1200px){.m-xl-0{margin:0!important}.mt-xl-0,.my-xl-0{margin-top:0!important}.mr-xl-0,.mx-xl-0{margin-right:0!important}.mb-xl-0,.my-xl-0{margin-bottom:0!important}.ml-xl-0,.mx-xl-0{margin-left:0!important}.m-xl-1{margin:.25rem!important}.mt-xl-1,.my-xl-1{margin-top:.25rem!important}.mr-xl-1,.mx-xl-1{margin-right:.25rem!important}.mb-xl-1,.my-xl-1{margin-bottom:.25rem!important}.ml-xl-1,.mx-xl-1{margin-left:.25rem!important}.m-xl-2{margin:.5rem!important}.mt-xl-2,.my-xl-2{margin-top:.5rem!important}.mr-xl-2,.mx-xl-2{margin-right:.5rem!important}.mb-xl-2,.my-xl-2{margin-bottom:.5rem!important}.ml-xl-2,.mx-xl-2{margin-left:.5rem!important}.m-xl-3{margin:1rem!important}.mt-xl-3,.my-xl-3{margin-top:1rem!important}.mr-xl-3,.mx-xl-3{margin-right:1rem!important}.mb-xl-3,.my-xl-3{margin-bottom:1rem!important}.ml-xl-3,.mx-xl-3{margin-left:1rem!important}.m-xl-4{margin:1.5rem!important}.mt-xl-4,.my-xl-4{margin-top:1.5rem!important}.mr-xl-4,.mx-xl-4{margin-right:1.5rem!important}.mb-xl-4,.my-xl-4{margin-bottom:1.5rem!important}.ml-xl-4,.mx-xl-4{margin-left:1.5rem!important}.m-xl-5{margin:3rem!important}.mt-xl-5,.my-xl-5{margin-top:3rem!important}.mr-xl-5,.mx-xl-5{margin-right:3rem!important}.mb-xl-5,.my-xl-5{margin-bottom:3rem!important}.ml-xl-5,.mx-xl-5{margin-left:3rem!important}.m-xl-6{margin:4rem!important}.mt-xl-6,.my-xl-6{margin-top:4rem!important}.mr-xl-6,.mx-xl-6{margin-right:4rem!important}.mb-xl-6,.my-xl-6{margin-bottom:4rem!important}.ml-xl-6,.mx-xl-6{margin-left:4rem!important}.p-xl-0{padding:0!important}.pt-xl-0,.py-xl-0{padding-top:0!important}.pr-xl-0,.px-xl-0{padding-right:0!important}.pb-xl-0,.py-xl-0{padding-bottom:0!important}.pl-xl-0,.px-xl-0{padding-left:0!important}.p-xl-1{padding:.25rem!important}.pt-xl-1,.py-xl-1{padding-top:.25rem!important}.pr-xl-1,.px-xl-1{padding-right:.25rem!important}.pb-xl-1,.py-xl-1{padding-bottom:.25rem!important}.pl-xl-1,.px-xl-1{padding-left:.25rem!important}.p-xl-2{padding:.5rem!important}.pt-xl-2,.py-xl-2{padding-top:.5rem!important}.pr-xl-2,.px-xl-2{padding-right:.5rem!important}.pb-xl-2,.py-xl-2{padding-bottom:.5rem!important}.pl-xl-2,.px-xl-2{padding-left:.5rem!important}.p-xl-3{padding:1rem!important}.pt-xl-3,.py-xl-3{padding-top:1rem!important}.pr-xl-3,.px-xl-3{padding-right:1rem!important}.pb-xl-3,.py-xl-3{padding-bottom:1rem!important}.pl-xl-3,.px-xl-3{padding-left:1rem!important}.p-xl-4{padding:1.5rem!important}.pt-xl-4,.py-xl-4{padding-top:1.5rem!important}.pr-xl-4,.px-xl-4{padding-right:1.5rem!important}.pb-xl-4,.py-xl-4{padding-bottom:1.5rem!important}.pl-xl-4,.px-xl-4{padding-left:1.5rem!important}.p-xl-5{padding:3rem!important}.pt-xl-5,.py-xl-5{padding-top:3rem!important}.pr-xl-5,.px-xl-5{padding-right:3rem!important}.pb-xl-5,.py-xl-5{padding-bottom:3rem!important}.pl-xl-5,.px-xl-5{padding-left:3rem!important}.p-xl-6{padding:4rem!important}.pt-xl-6,.py-xl-6{padding-top:4rem!important}.pr-xl-6,.px-xl-6{padding-right:4rem!important}.pb-xl-6,.py-xl-6{padding-bottom:4rem!important}.pl-xl-6,.px-xl-6{padding-left:4rem!important}.m-xl-n1{margin:-.25rem!important}.mt-xl-n1,.my-xl-n1{margin-top:-.25rem!important}.mr-xl-n1,.mx-xl-n1{margin-right:-.25rem!important}.mb-xl-n1,.my-xl-n1{margin-bottom:-.25rem!important}.ml-xl-n1,.mx-xl-n1{margin-left:-.25rem!important}.m-xl-n2{margin:-.5rem!important}.mt-xl-n2,.my-xl-n2{margin-top:-.5rem!important}.mr-xl-n2,.mx-xl-n2{margin-right:-.5rem!important}.mb-xl-n2,.my-xl-n2{margin-bottom:-.5rem!important}.ml-xl-n2,.mx-xl-n2{margin-left:-.5rem!important}.m-xl-n3{margin:-1rem!important}.mt-xl-n3,.my-xl-n3{margin-top:-1rem!important}.mr-xl-n3,.mx-xl-n3{margin-right:-1rem!important}.mb-xl-n3,.my-xl-n3{margin-bottom:-1rem!important}.ml-xl-n3,.mx-xl-n3{margin-left:-1rem!important}.m-xl-n4{margin:-1.5rem!important}.mt-xl-n4,.my-xl-n4{margin-top:-1.5rem!important}.mr-xl-n4,.mx-xl-n4{margin-right:-1.5rem!important}.mb-xl-n4,.my-xl-n4{margin-bottom:-1.5rem!important}.ml-xl-n4,.mx-xl-n4{margin-left:-1.5rem!important}.m-xl-n5{margin:-3rem!important}.mt-xl-n5,.my-xl-n5{margin-top:-3rem!important}.mr-xl-n5,.mx-xl-n5{margin-right:-3rem!important}.mb-xl-n5,.my-xl-n5{margin-bottom:-3rem!important}.ml-xl-n5,.mx-xl-n5{margin-left:-3rem!important}.m-xl-n6{margin:-4rem!important}.mt-xl-n6,.my-xl-n6{margin-top:-4rem!important}.mr-xl-n6,.mx-xl-n6{margin-right:-4rem!important}.mb-xl-n6,.my-xl-n6{margin-bottom:-4rem!important}.ml-xl-n6,.mx-xl-n6{margin-left:-4rem!important}.m-xl-auto{margin:auto!important}.mt-xl-auto,.my-xl-auto{margin-top:auto!important}.mr-xl-auto,.mx-xl-auto{margin-right:auto!important}.mb-xl-auto,.my-xl-auto{margin-bottom:auto!important}.ml-xl-auto,.mx-xl-auto{margin-left:auto!important}}.stretched-link::after{position:absolute;top:0;right:0;bottom:0;left:0;z-index:1;pointer-events:auto;content:"";background-color:rgba(0,0,0,0)}.text-monospace{font-family:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace!important}.text-justify{text-align:justify!important}.text-wrap{white-space:normal!important}.text-nowrap{white-space:nowrap!important}.text-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.text-left{text-align:left!important}.text-right{text-align:right!important}.text-center{text-align:center!important}@media (min-width:576px){.text-sm-left{text-align:left!important}.text-sm-right{text-align:right!important}.text-sm-center{text-align:center!important}}@media (min-width:768px){.text-md-left{text-align:left!important}.text-md-right{text-align:right!important}.text-md-center{text-align:center!important}}@media (min-width:992px){.text-lg-left{text-align:left!important}.text-lg-right{text-align:right!important}.text-lg-center{text-align:center!important}}@media (min-width:1200px){.text-xl-left{text-align:left!important}.text-xl-right{text-align:right!important}.text-xl-center{text-align:center!important}}.text-lowercase{text-transform:lowercase!important}.text-uppercase{text-transform:uppercase!important}.text-capitalize{text-transform:capitalize!important}.font-weight-light{font-weight:300!important}.font-weight-lighter{font-weight:lighter!important}.font-weight-normal{font-weight:400!important}.font-weight-bold{font-weight:700!important}.font-weight-bolder{font-weight:bolder!important}.font-italic{font-style:italic!important}.text-white{color:#fff!important}.text-primary{color:#1377c3!important}a.text-primary:focus,a.text-primary:hover{color:#0c4c7d!important}.text-primarystrong{color:#0c4c7d!important}a.text-primarystrong:focus,a.text-primarystrong:hover{color:#052237!important}.text-secondary{color:#677689!important}a.text-secondary:focus,a.text-secondary:hover{color:#46505d!important}.text-success{color:#218739!important}a.text-success:focus,a.text-success:hover{color:#124a1f!important}.text-info{color:#17a2b8!important}a.text-info:focus,a.text-info:hover{color:#0f6674!important}.text-warning{color:#ffc107!important}a.text-warning:focus,a.text-warning:hover{color:#ba8b00!important}.text-danger{color:#dc3545!important}a.text-danger:focus,a.text-danger:hover{color:#a71d2a!important}.text-light{color:#f8f9fa!important}a.text-light:focus,a.text-light:hover{color:#cbd3da!important}.text-dark{color:#343a40!important}a.text-dark:focus,a.text-dark:hover{color:#121416!important}.text-accentprimary{color:#0e558b!important}a.text-accentprimary:focus,a.text-accentprimary:hover{color:#072a46!important}.text-secondarylight{color:#6c727f!important}a.text-secondarylight:focus,a.text-secondarylight:hover{color:#494d56!important}.text-body{color:#212529!important}.text-muted{color:#6c757d!important}.text-black-50{color:rgba(0,0,0,.5)!important}.text-white-50{color:rgba(255,255,255,.5)!important}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.text-decoration-none{text-decoration:none!important}.text-break{word-wrap:break-word!important}.text-reset{color:inherit!important}.visible{visibility:visible!important}.invisible{visibility:hidden!important}.fade{transition:opacity .15s linear}@media (prefers-reduced-motion:reduce){.fade{transition:none}}.fade:not(.show){opacity:0}.collapse:not(.show){display:none}.collapsing{position:relative;height:0;overflow:hidden;transition:height .35s ease}@media (prefers-reduced-motion:reduce){.collapsing{transition:none}}.container{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:576px){.container{max-width:540px}}@media (min-width:768px){.container{max-width:720px}}@media (min-width:992px){.container{max-width:960px}}@media (min-width:1200px){.container{max-width:1140px}}.container-fluid,.container-lg,.container-md,.container-sm,.container-xl{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:576px){.container,.container-sm{max-width:540px}}@media (min-width:768px){.container,.container-md,.container-sm{max-width:720px}}@media (min-width:992px){.container,.container-lg,.container-md,.container-sm{max-width:960px}}@media (min-width:1200px){.container,.container-lg,.container-md,.container-sm,.container-xl{max-width:1140px}}.row{display:flex;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.no-gutters{margin-right:0;margin-left:0}.no-gutters>.col,.no-gutters>[class*=col-]{padding-right:0;padding-left:0}.col,.col-1,.col-10,.col-11,.col-12,.col-2,.col-3,.col-4,.col-5,.col-6,.col-7,.col-8,.col-9,.col-auto,.col-lg,.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-lg-auto,.col-md,.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-md-auto,.col-sm,.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-sm-auto,.col-xl,.col-xl-1,.col-xl-10,.col-xl-11,.col-xl-12,.col-xl-2,.col-xl-3,.col-xl-4,.col-xl-5,.col-xl-6,.col-xl-7,.col-xl-8,.col-xl-9,.col-xl-auto{position:relative;width:100%;padding-right:15px;padding-left:15px}.col{flex-basis:0;flex-grow:1;min-width:0;max-width:100%}.row-cols-1>*{flex:0 0 100%;max-width:100%}.row-cols-2>*{flex:0 0 50%;max-width:50%}.row-cols-3>*{flex:0 0 33.3333333333%;max-width:33.3333333333%}.row-cols-4>*{flex:0 0 25%;max-width:25%}.row-cols-5>*{flex:0 0 20%;max-width:20%}.row-cols-6>*{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-auto{flex:0 0 auto;width:auto;max-width:100%}.col-1{flex:0 0 8.3333333333%;max-width:8.3333333333%}.col-2{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-3{flex:0 0 25%;max-width:25%}.col-4{flex:0 0 33.3333333333%;max-width:33.3333333333%}.col-5{flex:0 0 41.6666666667%;max-width:41.6666666667%}.col-6{flex:0 0 50%;max-width:50%}.col-7{flex:0 0 58.3333333333%;max-width:58.3333333333%}.col-8{flex:0 0 66.6666666667%;max-width:66.6666666667%}.col-9{flex:0 0 75%;max-width:75%}.col-10{flex:0 0 83.3333333333%;max-width:83.3333333333%}.col-11{flex:0 0 91.6666666667%;max-width:91.6666666667%}.col-12{flex:0 0 100%;max-width:100%}.order-first{order:-1}.order-last{order:13}.order-0{order:0}.order-1{order:1}.order-2{order:2}.order-3{order:3}.order-4{order:4}.order-5{order:5}.order-6{order:6}.order-7{order:7}.order-8{order:8}.order-9{order:9}.order-10{order:10}.order-11{order:11}.order-12{order:12}.offset-1{margin-left:8.3333333333%}.offset-2{margin-left:16.6666666667%}.offset-3{margin-left:25%}.offset-4{margin-left:33.3333333333%}.offset-5{margin-left:41.6666666667%}.offset-6{margin-left:50%}.offset-7{margin-left:58.3333333333%}.offset-8{margin-left:66.6666666667%}.offset-9{margin-left:75%}.offset-10{margin-left:83.3333333333%}.offset-11{margin-left:91.6666666667%}@media (min-width:576px){.col-sm{flex-basis:0;flex-grow:1;min-width:0;max-width:100%}.row-cols-sm-1>*{flex:0 0 100%;max-width:100%}.row-cols-sm-2>*{flex:0 0 50%;max-width:50%}.row-cols-sm-3>*{flex:0 0 33.3333333333%;max-width:33.3333333333%}.row-cols-sm-4>*{flex:0 0 25%;max-width:25%}.row-cols-sm-5>*{flex:0 0 20%;max-width:20%}.row-cols-sm-6>*{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-sm-auto{flex:0 0 auto;width:auto;max-width:100%}.col-sm-1{flex:0 0 8.3333333333%;max-width:8.3333333333%}.col-sm-2{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-sm-3{flex:0 0 25%;max-width:25%}.col-sm-4{flex:0 0 33.3333333333%;max-width:33.3333333333%}.col-sm-5{flex:0 0 41.6666666667%;max-width:41.6666666667%}.col-sm-6{flex:0 0 50%;max-width:50%}.col-sm-7{flex:0 0 58.3333333333%;max-width:58.3333333333%}.col-sm-8{flex:0 0 66.6666666667%;max-width:66.6666666667%}.col-sm-9{flex:0 0 75%;max-width:75%}.col-sm-10{flex:0 0 83.3333333333%;max-width:83.3333333333%}.col-sm-11{flex:0 0 91.6666666667%;max-width:91.6666666667%}.col-sm-12{flex:0 0 100%;max-width:100%}.order-sm-first{order:-1}.order-sm-last{order:13}.order-sm-0{order:0}.order-sm-1{order:1}.order-sm-2{order:2}.order-sm-3{order:3}.order-sm-4{order:4}.order-sm-5{order:5}.order-sm-6{order:6}.order-sm-7{order:7}.order-sm-8{order:8}.order-sm-9{order:9}.order-sm-10{order:10}.order-sm-11{order:11}.order-sm-12{order:12}.offset-sm-0{margin-left:0}.offset-sm-1{margin-left:8.3333333333%}.offset-sm-2{margin-left:16.6666666667%}.offset-sm-3{margin-left:25%}.offset-sm-4{margin-left:33.3333333333%}.offset-sm-5{margin-left:41.6666666667%}.offset-sm-6{margin-left:50%}.offset-sm-7{margin-left:58.3333333333%}.offset-sm-8{margin-left:66.6666666667%}.offset-sm-9{margin-left:75%}.offset-sm-10{margin-left:83.3333333333%}.offset-sm-11{margin-left:91.6666666667%}}@media (min-width:768px){.col-md{flex-basis:0;flex-grow:1;min-width:0;max-width:100%}.row-cols-md-1>*{flex:0 0 100%;max-width:100%}.row-cols-md-2>*{flex:0 0 50%;max-width:50%}.row-cols-md-3>*{flex:0 0 33.3333333333%;max-width:33.3333333333%}.row-cols-md-4>*{flex:0 0 25%;max-width:25%}.row-cols-md-5>*{flex:0 0 20%;max-width:20%}.row-cols-md-6>*{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-md-auto{flex:0 0 auto;width:auto;max-width:100%}.col-md-1{flex:0 0 8.3333333333%;max-width:8.3333333333%}.col-md-2{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-md-3{flex:0 0 25%;max-width:25%}.col-md-4{flex:0 0 33.3333333333%;max-width:33.3333333333%}.col-md-5{flex:0 0 41.6666666667%;max-width:41.6666666667%}.col-md-6{flex:0 0 50%;max-width:50%}.col-md-7{flex:0 0 58.3333333333%;max-width:58.3333333333%}.col-md-8{flex:0 0 66.6666666667%;max-width:66.6666666667%}.col-md-9{flex:0 0 75%;max-width:75%}.col-md-10{flex:0 0 83.3333333333%;max-width:83.3333333333%}.col-md-11{flex:0 0 91.6666666667%;max-width:91.6666666667%}.col-md-12{flex:0 0 100%;max-width:100%}.order-md-first{order:-1}.order-md-last{order:13}.order-md-0{order:0}.order-md-1{order:1}.order-md-2{order:2}.order-md-3{order:3}.order-md-4{order:4}.order-md-5{order:5}.order-md-6{order:6}.order-md-7{order:7}.order-md-8{order:8}.order-md-9{order:9}.order-md-10{order:10}.order-md-11{order:11}.order-md-12{order:12}.offset-md-0{margin-left:0}.offset-md-1{margin-left:8.3333333333%}.offset-md-2{margin-left:16.6666666667%}.offset-md-3{margin-left:25%}.offset-md-4{margin-left:33.3333333333%}.offset-md-5{margin-left:41.6666666667%}.offset-md-6{margin-left:50%}.offset-md-7{margin-left:58.3333333333%}.offset-md-8{margin-left:66.6666666667%}.offset-md-9{margin-left:75%}.offset-md-10{margin-left:83.3333333333%}.offset-md-11{margin-left:91.6666666667%}}@media (min-width:992px){.col-lg{flex-basis:0;flex-grow:1;min-width:0;max-width:100%}.row-cols-lg-1>*{flex:0 0 100%;max-width:100%}.row-cols-lg-2>*{flex:0 0 50%;max-width:50%}.row-cols-lg-3>*{flex:0 0 33.3333333333%;max-width:33.3333333333%}.row-cols-lg-4>*{flex:0 0 25%;max-width:25%}.row-cols-lg-5>*{flex:0 0 20%;max-width:20%}.row-cols-lg-6>*{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-lg-auto{flex:0 0 auto;width:auto;max-width:100%}.col-lg-1{flex:0 0 8.3333333333%;max-width:8.3333333333%}.col-lg-2{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-lg-3{flex:0 0 25%;max-width:25%}.col-lg-4{flex:0 0 33.3333333333%;max-width:33.3333333333%}.col-lg-5{flex:0 0 41.6666666667%;max-width:41.6666666667%}.col-lg-6{flex:0 0 50%;max-width:50%}.col-lg-7{flex:0 0 58.3333333333%;max-width:58.3333333333%}.col-lg-8{flex:0 0 66.6666666667%;max-width:66.6666666667%}.col-lg-9{flex:0 0 75%;max-width:75%}.col-lg-10{flex:0 0 83.3333333333%;max-width:83.3333333333%}.col-lg-11{flex:0 0 91.6666666667%;max-width:91.6666666667%}.col-lg-12{flex:0 0 100%;max-width:100%}.order-lg-first{order:-1}.order-lg-last{order:13}.order-lg-0{order:0}.order-lg-1{order:1}.order-lg-2{order:2}.order-lg-3{order:3}.order-lg-4{order:4}.order-lg-5{order:5}.order-lg-6{order:6}.order-lg-7{order:7}.order-lg-8{order:8}.order-lg-9{order:9}.order-lg-10{order:10}.order-lg-11{order:11}.order-lg-12{order:12}.offset-lg-0{margin-left:0}.offset-lg-1{margin-left:8.3333333333%}.offset-lg-2{margin-left:16.6666666667%}.offset-lg-3{margin-left:25%}.offset-lg-4{margin-left:33.3333333333%}.offset-lg-5{margin-left:41.6666666667%}.offset-lg-6{margin-left:50%}.offset-lg-7{margin-left:58.3333333333%}.offset-lg-8{margin-left:66.6666666667%}.offset-lg-9{margin-left:75%}.offset-lg-10{margin-left:83.3333333333%}.offset-lg-11{margin-left:91.6666666667%}}@media (min-width:1200px){.col-xl{flex-basis:0;flex-grow:1;min-width:0;max-width:100%}.row-cols-xl-1>*{flex:0 0 100%;max-width:100%}.row-cols-xl-2>*{flex:0 0 50%;max-width:50%}.row-cols-xl-3>*{flex:0 0 33.3333333333%;max-width:33.3333333333%}.row-cols-xl-4>*{flex:0 0 25%;max-width:25%}.row-cols-xl-5>*{flex:0 0 20%;max-width:20%}.row-cols-xl-6>*{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-xl-auto{flex:0 0 auto;width:auto;max-width:100%}.col-xl-1{flex:0 0 8.3333333333%;max-width:8.3333333333%}.col-xl-2{flex:0 0 16.6666666667%;max-width:16.6666666667%}.col-xl-3{flex:0 0 25%;max-width:25%}.col-xl-4{flex:0 0 33.3333333333%;max-width:33.3333333333%}.col-xl-5{flex:0 0 41.6666666667%;max-width:41.6666666667%}.col-xl-6{flex:0 0 50%;max-width:50%}.col-xl-7{flex:0 0 58.3333333333%;max-width:58.3333333333%}.col-xl-8{flex:0 0 66.6666666667%;max-width:66.6666666667%}.col-xl-9{flex:0 0 75%;max-width:75%}.col-xl-10{flex:0 0 83.3333333333%;max-width:83.3333333333%}.col-xl-11{flex:0 0 91.6666666667%;max-width:91.6666666667%}.col-xl-12{flex:0 0 100%;max-width:100%}.order-xl-first{order:-1}.order-xl-last{order:13}.order-xl-0{order:0}.order-xl-1{order:1}.order-xl-2{order:2}.order-xl-3{order:3}.order-xl-4{order:4}.order-xl-5{order:5}.order-xl-6{order:6}.order-xl-7{order:7}.order-xl-8{order:8}.order-xl-9{order:9}.order-xl-10{order:10}.order-xl-11{order:11}.order-xl-12{order:12}.offset-xl-0{margin-left:0}.offset-xl-1{margin-left:8.3333333333%}.offset-xl-2{margin-left:16.6666666667%}.offset-xl-3{margin-left:25%}.offset-xl-4{margin-left:33.3333333333%}.offset-xl-5{margin-left:41.6666666667%}.offset-xl-6{margin-left:50%}.offset-xl-7{margin-left:58.3333333333%}.offset-xl-8{margin-left:66.6666666667%}.offset-xl-9{margin-left:75%}.offset-xl-10{margin-left:83.3333333333%}.offset-xl-11{margin-left:91.6666666667%}}.btn{display:inline-block;font-weight:400;color:#212529;text-align:center;vertical-align:middle;-webkit-user-select:none;-moz-user-select:none;user-select:none;background-color:transparent;border:1px solid transparent;padding:.375rem .75rem;font-size:1rem;line-height:1.5;border-radius:.15rem;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.btn{transition:none}}.btn:hover{color:#212529;text-decoration:none}.btn.focus,.btn:focus{outline:0;box-shadow:0 0 0 .2rem rgba(19,119,195,.25)}.btn.disabled,.btn:disabled{opacity:.65}.btn:not(:disabled):not(.disabled){cursor:pointer}a.btn.disabled,fieldset:disabled a.btn{pointer-events:none}.btn-primary{color:#fff;background-color:#1377c3;border-color:#1377c3}.btn-primary:hover{color:#fff;background-color:#1062a0;border-color:#0e5b95}.btn-primary.focus,.btn-primary:focus{color:#fff;background-color:#1062a0;border-color:#0e5b95;box-shadow:0 0 0 .2rem rgba(54,139,204,.5)}.btn-primary.disabled,.btn-primary:disabled{color:#fff;background-color:#1377c3;border-color:#1377c3}.btn-primary:not(:disabled):not(.disabled).active,.btn-primary:not(:disabled):not(.disabled):active,.show>.btn-primary.dropdown-toggle{color:#fff;background-color:#0e5b95;border-color:#0d5489}.btn-primary:not(:disabled):not(.disabled).active:focus,.btn-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-primary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(54,139,204,.5)}.btn-primarystrong{color:#fff;background-color:#0c4c7d;border-color:#0c4c7d}.btn-primarystrong:hover{color:#fff;background-color:#09375a;border-color:#08304e}.btn-primarystrong.focus,.btn-primarystrong:focus{color:#fff;background-color:#09375a;border-color:#08304e;box-shadow:0 0 0 .2rem rgba(48,103,145,.5)}.btn-primarystrong.disabled,.btn-primarystrong:disabled{color:#fff;background-color:#0c4c7d;border-color:#0c4c7d}.btn-primarystrong:not(:disabled):not(.disabled).active,.btn-primarystrong:not(:disabled):not(.disabled):active,.show>.btn-primarystrong.dropdown-toggle{color:#fff;background-color:#08304e;border-color:#062943}.btn-primarystrong:not(:disabled):not(.disabled).active:focus,.btn-primarystrong:not(:disabled):not(.disabled):active:focus,.show>.btn-primarystrong.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(48,103,145,.5)}.btn-secondary{color:#fff;background-color:#677689;border-color:#677689}.btn-secondary:hover{color:#fff;background-color:#576373;border-color:#515d6c}.btn-secondary.focus,.btn-secondary:focus{color:#fff;background-color:#576373;border-color:#515d6c;box-shadow:0 0 0 .2rem rgba(126,139,155,.5)}.btn-secondary.disabled,.btn-secondary:disabled{color:#fff;background-color:#677689;border-color:#677689}.btn-secondary:not(:disabled):not(.disabled).active,.btn-secondary:not(:disabled):not(.disabled):active,.show>.btn-secondary.dropdown-toggle{color:#fff;background-color:#515d6c;border-color:#4c5765}.btn-secondary:not(:disabled):not(.disabled).active:focus,.btn-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-secondary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(126,139,155,.5)}.btn-success{color:#fff;background-color:#218739;border-color:#218739}.btn-success:hover{color:#fff;background-color:#19682c;border-color:#175e28}.btn-success.focus,.btn-success:focus{color:#fff;background-color:#19682c;border-color:#175e28;box-shadow:0 0 0 .2rem rgba(66,153,87,.5)}.btn-success.disabled,.btn-success:disabled{color:#fff;background-color:#218739;border-color:#218739}.btn-success:not(:disabled):not(.disabled).active,.btn-success:not(:disabled):not(.disabled):active,.show>.btn-success.dropdown-toggle{color:#fff;background-color:#175e28;border-color:#145423}.btn-success:not(:disabled):not(.disabled).active:focus,.btn-success:not(:disabled):not(.disabled):active:focus,.show>.btn-success.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(66,153,87,.5)}.btn-info{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-info:hover{color:#fff;background-color:#138496;border-color:#117a8b}.btn-info.focus,.btn-info:focus{color:#fff;background-color:#138496;border-color:#117a8b;box-shadow:0 0 0 .2rem rgba(58,176,195,.5)}.btn-info.disabled,.btn-info:disabled{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-info:not(:disabled):not(.disabled).active,.btn-info:not(:disabled):not(.disabled):active,.show>.btn-info.dropdown-toggle{color:#fff;background-color:#117a8b;border-color:#10707f}.btn-info:not(:disabled):not(.disabled).active:focus,.btn-info:not(:disabled):not(.disabled):active:focus,.show>.btn-info.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(58,176,195,.5)}.btn-warning{color:#fff;background-color:#ffc107;border-color:#ffc107}.btn-warning:hover{color:#fff;background-color:#e0a800;border-color:#d39e00}.btn-warning.focus,.btn-warning:focus{color:#fff;background-color:#e0a800;border-color:#d39e00;box-shadow:0 0 0 .2rem rgba(255,202,44,.5)}.btn-warning.disabled,.btn-warning:disabled{color:#fff;background-color:#ffc107;border-color:#ffc107}.btn-warning:not(:disabled):not(.disabled).active,.btn-warning:not(:disabled):not(.disabled):active,.show>.btn-warning.dropdown-toggle{color:#fff;background-color:#d39e00;border-color:#c69500}.btn-warning:not(:disabled):not(.disabled).active:focus,.btn-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-warning.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(255,202,44,.5)}.btn-danger{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-danger:hover{color:#fff;background-color:#c82333;border-color:#bd2130}.btn-danger.focus,.btn-danger:focus{color:#fff;background-color:#c82333;border-color:#bd2130;box-shadow:0 0 0 .2rem rgba(225,83,97,.5)}.btn-danger.disabled,.btn-danger:disabled{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-danger:not(:disabled):not(.disabled).active,.btn-danger:not(:disabled):not(.disabled):active,.show>.btn-danger.dropdown-toggle{color:#fff;background-color:#bd2130;border-color:#b21f2d}.btn-danger:not(:disabled):not(.disabled).active:focus,.btn-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-danger.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(225,83,97,.5)}.btn-light{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:hover{color:#212529;background-color:#e2e6ea;border-color:#dae0e5}.btn-light.focus,.btn-light:focus{color:#212529;background-color:#e2e6ea;border-color:#dae0e5;box-shadow:0 0 0 .2rem rgba(216,217,219,.5)}.btn-light.disabled,.btn-light:disabled{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:not(:disabled):not(.disabled).active,.btn-light:not(:disabled):not(.disabled):active,.show>.btn-light.dropdown-toggle{color:#212529;background-color:#dae0e5;border-color:#d3d9df}.btn-light:not(:disabled):not(.disabled).active:focus,.btn-light:not(:disabled):not(.disabled):active:focus,.show>.btn-light.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(216,217,219,.5)}.btn-dark{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:hover{color:#fff;background-color:#23272b;border-color:#1d2124}.btn-dark.focus,.btn-dark:focus{color:#fff;background-color:#23272b;border-color:#1d2124;box-shadow:0 0 0 .2rem rgba(82,88,93,.5)}.btn-dark.disabled,.btn-dark:disabled{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:not(:disabled):not(.disabled).active,.btn-dark:not(:disabled):not(.disabled):active,.show>.btn-dark.dropdown-toggle{color:#fff;background-color:#1d2124;border-color:#171a1d}.btn-dark:not(:disabled):not(.disabled).active:focus,.btn-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-dark.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(82,88,93,.5)}.btn-accentprimary{color:#fff;background-color:#0e558b;border-color:#0e558b}.btn-accentprimary:hover{color:#fff;background-color:#0a4068;border-color:#09395d}.btn-accentprimary.focus,.btn-accentprimary:focus{color:#fff;background-color:#0a4068;border-color:#09395d;box-shadow:0 0 0 .2rem rgba(50,111,156,.5)}.btn-accentprimary.disabled,.btn-accentprimary:disabled{color:#fff;background-color:#0e558b;border-color:#0e558b}.btn-accentprimary:not(:disabled):not(.disabled).active,.btn-accentprimary:not(:disabled):not(.disabled):active,.show>.btn-accentprimary.dropdown-toggle{color:#fff;background-color:#09395d;border-color:#083251}.btn-accentprimary:not(:disabled):not(.disabled).active:focus,.btn-accentprimary:not(:disabled):not(.disabled):active:focus,.show>.btn-accentprimary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(50,111,156,.5)}.btn-secondarylight{color:#fff;background-color:#6c727f;border-color:#6c727f}.btn-secondarylight:hover{color:#fff;background-color:#5a5f6a;border-color:#555963}.btn-secondarylight.focus,.btn-secondarylight:focus{color:#fff;background-color:#5a5f6a;border-color:#555963;box-shadow:0 0 0 .2rem rgba(130,135,146,.5)}.btn-secondarylight.disabled,.btn-secondarylight:disabled{color:#fff;background-color:#6c727f;border-color:#6c727f}.btn-secondarylight:not(:disabled):not(.disabled).active,.btn-secondarylight:not(:disabled):not(.disabled):active,.show>.btn-secondarylight.dropdown-toggle{color:#fff;background-color:#555963;border-color:#4f535d}.btn-secondarylight:not(:disabled):not(.disabled).active:focus,.btn-secondarylight:not(:disabled):not(.disabled):active:focus,.show>.btn-secondarylight.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(130,135,146,.5)}.btn-outline-primary{color:#1377c3;border-color:#1377c3}.btn-outline-primary:hover{color:#fff;background-color:#1377c3;border-color:#1377c3}.btn-outline-primary.focus,.btn-outline-primary:focus{box-shadow:0 0 0 .2rem rgba(19,119,195,.5)}.btn-outline-primary.disabled,.btn-outline-primary:disabled{color:#1377c3;background-color:transparent}.btn-outline-primary:not(:disabled):not(.disabled).active,.btn-outline-primary:not(:disabled):not(.disabled):active,.show>.btn-outline-primary.dropdown-toggle{color:#fff;background-color:#1377c3;border-color:#1377c3}.btn-outline-primary:not(:disabled):not(.disabled).active:focus,.btn-outline-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-primary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(19,119,195,.5)}.btn-outline-primarystrong{color:#0c4c7d;border-color:#0c4c7d}.btn-outline-primarystrong:hover{color:#fff;background-color:#0c4c7d;border-color:#0c4c7d}.btn-outline-primarystrong.focus,.btn-outline-primarystrong:focus{box-shadow:0 0 0 .2rem rgba(12,76,125,.5)}.btn-outline-primarystrong.disabled,.btn-outline-primarystrong:disabled{color:#0c4c7d;background-color:transparent}.btn-outline-primarystrong:not(:disabled):not(.disabled).active,.btn-outline-primarystrong:not(:disabled):not(.disabled):active,.show>.btn-outline-primarystrong.dropdown-toggle{color:#fff;background-color:#0c4c7d;border-color:#0c4c7d}.btn-outline-primarystrong:not(:disabled):not(.disabled).active:focus,.btn-outline-primarystrong:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-primarystrong.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(12,76,125,.5)}.btn-outline-secondary{color:#677689;border-color:#677689}.btn-outline-secondary:hover{color:#fff;background-color:#677689;border-color:#677689}.btn-outline-secondary.focus,.btn-outline-secondary:focus{box-shadow:0 0 0 .2rem rgba(103,118,137,.5)}.btn-outline-secondary.disabled,.btn-outline-secondary:disabled{color:#677689;background-color:transparent}.btn-outline-secondary:not(:disabled):not(.disabled).active,.btn-outline-secondary:not(:disabled):not(.disabled):active,.show>.btn-outline-secondary.dropdown-toggle{color:#fff;background-color:#677689;border-color:#677689}.btn-outline-secondary:not(:disabled):not(.disabled).active:focus,.btn-outline-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-secondary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(103,118,137,.5)}.btn-outline-success{color:#218739;border-color:#218739}.btn-outline-success:hover{color:#fff;background-color:#218739;border-color:#218739}.btn-outline-success.focus,.btn-outline-success:focus{box-shadow:0 0 0 .2rem rgba(33,135,57,.5)}.btn-outline-success.disabled,.btn-outline-success:disabled{color:#218739;background-color:transparent}.btn-outline-success:not(:disabled):not(.disabled).active,.btn-outline-success:not(:disabled):not(.disabled):active,.show>.btn-outline-success.dropdown-toggle{color:#fff;background-color:#218739;border-color:#218739}.btn-outline-success:not(:disabled):not(.disabled).active:focus,.btn-outline-success:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-success.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(33,135,57,.5)}.btn-outline-info{color:#17a2b8;border-color:#17a2b8}.btn-outline-info:hover{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-outline-info.focus,.btn-outline-info:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-outline-info.disabled,.btn-outline-info:disabled{color:#17a2b8;background-color:transparent}.btn-outline-info:not(:disabled):not(.disabled).active,.btn-outline-info:not(:disabled):not(.disabled):active,.show>.btn-outline-info.dropdown-toggle{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-outline-info:not(:disabled):not(.disabled).active:focus,.btn-outline-info:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-info.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-outline-warning{color:#ffc107;border-color:#ffc107}.btn-outline-warning:hover{color:#fff;background-color:#ffc107;border-color:#ffc107}.btn-outline-warning.focus,.btn-outline-warning:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-outline-warning.disabled,.btn-outline-warning:disabled{color:#ffc107;background-color:transparent}.btn-outline-warning:not(:disabled):not(.disabled).active,.btn-outline-warning:not(:disabled):not(.disabled):active,.show>.btn-outline-warning.dropdown-toggle{color:#fff;background-color:#ffc107;border-color:#ffc107}.btn-outline-warning:not(:disabled):not(.disabled).active:focus,.btn-outline-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-warning.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-outline-danger{color:#dc3545;border-color:#dc3545}.btn-outline-danger:hover{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-outline-danger.focus,.btn-outline-danger:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-outline-danger.disabled,.btn-outline-danger:disabled{color:#dc3545;background-color:transparent}.btn-outline-danger:not(:disabled):not(.disabled).active,.btn-outline-danger:not(:disabled):not(.disabled):active,.show>.btn-outline-danger.dropdown-toggle{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-outline-danger:not(:disabled):not(.disabled).active:focus,.btn-outline-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-danger.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-outline-light{color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light:hover{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light.focus,.btn-outline-light:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-light.disabled,.btn-outline-light:disabled{color:#f8f9fa;background-color:transparent}.btn-outline-light:not(:disabled):not(.disabled).active,.btn-outline-light:not(:disabled):not(.disabled):active,.show>.btn-outline-light.dropdown-toggle{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light:not(:disabled):not(.disabled).active:focus,.btn-outline-light:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-light.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-dark{color:#343a40;border-color:#343a40}.btn-outline-dark:hover{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark.focus,.btn-outline-dark:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-dark.disabled,.btn-outline-dark:disabled{color:#343a40;background-color:transparent}.btn-outline-dark:not(:disabled):not(.disabled).active,.btn-outline-dark:not(:disabled):not(.disabled):active,.show>.btn-outline-dark.dropdown-toggle{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark:not(:disabled):not(.disabled).active:focus,.btn-outline-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-dark.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-accentprimary{color:#0e558b;border-color:#0e558b}.btn-outline-accentprimary:hover{color:#fff;background-color:#0e558b;border-color:#0e558b}.btn-outline-accentprimary.focus,.btn-outline-accentprimary:focus{box-shadow:0 0 0 .2rem rgba(14,85,139,.5)}.btn-outline-accentprimary.disabled,.btn-outline-accentprimary:disabled{color:#0e558b;background-color:transparent}.btn-outline-accentprimary:not(:disabled):not(.disabled).active,.btn-outline-accentprimary:not(:disabled):not(.disabled):active,.show>.btn-outline-accentprimary.dropdown-toggle{color:#fff;background-color:#0e558b;border-color:#0e558b}.btn-outline-accentprimary:not(:disabled):not(.disabled).active:focus,.btn-outline-accentprimary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-accentprimary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(14,85,139,.5)}.btn-outline-secondarylight{color:#6c727f;border-color:#6c727f}.btn-outline-secondarylight:hover{color:#fff;background-color:#6c727f;border-color:#6c727f}.btn-outline-secondarylight.focus,.btn-outline-secondarylight:focus{box-shadow:0 0 0 .2rem rgba(108,114,127,.5)}.btn-outline-secondarylight.disabled,.btn-outline-secondarylight:disabled{color:#6c727f;background-color:transparent}.btn-outline-secondarylight:not(:disabled):not(.disabled).active,.btn-outline-secondarylight:not(:disabled):not(.disabled):active,.show>.btn-outline-secondarylight.dropdown-toggle{color:#fff;background-color:#6c727f;border-color:#6c727f}.btn-outline-secondarylight:not(:disabled):not(.disabled).active:focus,.btn-outline-secondarylight:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-secondarylight.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(108,114,127,.5)}.btn-link{font-weight:400;color:#1377c3;text-decoration:none}.btn-link:hover{color:#0c4c7d;text-decoration:underline}.btn-link.focus,.btn-link:focus{text-decoration:underline}.btn-link.disabled,.btn-link:disabled{color:#6c757d;pointer-events:none}.btn-lg{padding:.5rem 1rem;font-size:1.25rem;line-height:1.5;border-radius:.3rem}.btn-sm{padding:.25rem .5rem;font-size:.875rem;line-height:1.5;border-radius:.2rem}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:.5rem}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}body{padding-top:4rem}body.navbarborder .navbar,body.scrolled .navbar{box-shadow:0 0 6px rgba(108,117,125,.5)}.navbar{background-color:#fff}.navbar #fmNavbarToggle{padding-top:6px}.navbar .navbar-logo{max-height:2.5rem}.navbar .navbar-nav .nav-item{margin-left:.75rem;line-height:38px}.navbar .navbar-nav .nav-item .btn{margin-left:.25em}@media (max-width:991.98px){.navbar .navbar-nav .nav-item{margin-left:0}}.navbar .navbar-nav .nav-item.muted .nav-link{opacity:.6!important}@media (min-width:992px){.navbar .navbar-nav .nav-item.foldable{position:relative}}.navbar .navbar-nav .nav-item i.fa-chevron-up{display:none}.navbar .navbar-nav .nav-item i.fa-chevron-down,.navbar .navbar-nav .nav-item i.fa-chevron-up{font-size:.9rem;width:1.25rem}.navbar .navbar-nav .nav-item.unfold i.fa-chevron-up{display:inline-block}.navbar .navbar-nav .nav-item.unfold i.fa-chevron-down{display:none}.navbar .navbar-nav .nav-link{transition:opacity .2s ease-in-out;color:#495057!important;padding:0 .5em;cursor:pointer}.navbar .navbar-nav .nav-link:hover{color:#000!important}.navbar .navbar-nav .dropdown-toggle{cursor:pointer}.navbar .navbar-nav .dropdown-toggle::after{display:none}.navbar .mega-menu{visibility:hidden;position:absolute;background-color:transparent;top:35px;left:0;transition:opacity .2s ease-in-out,visibility .2s ease-in-out;opacity:0;max-width:1140px}@media (max-width:991.98px){.navbar .mega-menu{max-width:932px}}.navbar .mega-menu .mega-menu-content{background-color:#fff;margin-top:20px;border:1px solid #ced4da;box-shadow:0 5px 15px rgba(0,0,0,.2);padding:1.5em;width:100%;display:flex;line-height:1.25em}.navbar .mega-menu .mega-menu-content.nowrap{white-space:nowrap}.navbar .mega-menu .mega-menu-content .mega-menu-col{flex-grow:1;padding-right:6em}.navbar .mega-menu .mega-menu-content .mega-menu-col ul{margin:0;padding:0}.navbar .mega-menu .mega-menu-content .mega-menu-col ul li{list-style:none;margin:.8em 0}.navbar .mega-menu .mega-menu-content .mega-menu-col i{margin-right:.8rem}.navbar .mega-menu .mega-menu-content p{font-weight:700;text-transform:uppercase;font-size:.9em}.navbar .mega-menu .mega-menu-content a{color:#495057!important}.navbar .mega-menu .mega-menu-content a:hover{color:#000!important;text-decoration:none}.navbar .mega-menu .mega-menu-content .dropdown-item{cursor:pointer;padding:.4em 2em .4em 1em;color:#495057!important}.navbar .mega-menu .mega-menu-content .dropdown-item i{color:#adb5bd!important}.navbar .mega-menu .mega-menu-content .dropdown-item.currentpage,.navbar .mega-menu .mega-menu-content .dropdown-item.currentpage i{color:#000!important;font-weight:700}.navbar .mega-menu .mega-menu-content .dropdown-item:hover{background:0 0}.navbar .mega-menu .mega-menu-content .dropdown-item:hover.emphasized,.navbar .mega-menu .mega-menu-content .dropdown-item:hover.emphasized i{font-weight:700}.navbar .mega-menu.unfold{visibility:visible;opacity:1}.navbar .mega-menu.fullwidth{width:1110px}@media (max-width:1200px){.navbar .mega-menu.fullwidth{width:930px}}.navbar .mega-menu.fullwidth .mega-menu-content .mega-menu-col{padding-right:1.5em}.text-small{font-size:.9rem!important}.text-mini{font-size:.8rem!important}.fake-link{color:#1377c3;cursor:pointer}.fake-link:hover{color:#1169ac}.ng-cloak,.x-ng-cloak,[data-ng-cloak],[ng-cloak],[ng\:cloak],[x-ng-cloak]{display:none!important}@media (max-width:991.98px){body.with-submenu{overflow:hidden!important}body.mainmenuopen #fmNavbar{padding-bottom:0}#fmNavbar .container{max-width:100%;width:100%;margin:0}#fmNavbar #fmNavbarToggle{padding:0;margin-top:8px;overflow-y:auto;overflow-x:hidden;max-height:calc(100vh - 60px);margin-left:-1rem!important;margin-right:-1rem!important}#fmNavbar #fmNavbarToggle.collapsing{overflow-y:hidden!important}#fmNavbar #fmNavbarToggle .navbar-nav{overflow:hidden}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item{font-size:1.25em;margin:0!important;border-top:1px solid #e9ecef;padding:.75rem 1rem}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .nav-link{padding:0!important}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu{height:0;display:none}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu.unfold{display:block;height:auto;position:relative;top:.5rem;margin-left:-1rem;margin-right:-1rem;margin-bottom:-.5rem}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu.unfold .mega-menu-content{box-shadow:none;border:none;background-color:#f8f9fa;margin-top:.25rem;padding:0;flex-direction:column}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu.unfold .mega-menu-content .mega-menu-col{padding:0}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu.unfold .mega-menu-content .mega-menu-col h5,#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .mega-menu.unfold .mega-menu-content .mega-menu-col ul li{margin:.8em}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .dropdown-divider,#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .fa-user-circle{display:none}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item .dropdown-item{padding:.75rem 1rem}#fmNavbar #fmNavbarToggle .navbar-nav .nav-item i.fa-chevron-down,#fmNavbar #fmNavbarToggle .navbar-nav .nav-item i.fa-chevron-up{float:right;font-size:1em;margin-top:10px}#fmNavbar #fmNavbarToggle .menu-storage .menu-storage-bar-wrap{height:18px}}</style>
<style>body,html.integrated body{padding-top:0}html.integrated,html.integrated body{background-color:transparent!important}html.integrated #background_cycler,html.integrated #download-footer,html.integrated #logoHolder,html.integrated body #background_cycler,html.integrated body #download-footer,html.integrated body #logoHolder{display:none!important}html.integrated #download-column,html.integrated body #download-column{padding:0!important;margin:0!important;width:100%!important}html.integrated #download-column #download-content,html.integrated body #download-column #download-content{padding:0!important}html.integrated .container,html.integrated body .container{max-width:100%!important}h1{font-size:1.5rem!important}#fmNavbar{display:none!important}.navbar-expand-lg>.container{padding:0 15px!important}.main-outercon{padding-top:0}.whiteHolder{background-color:#f8f9fa;border-radius:0}h4{font-size:1.5rem;font-weight:700;color:#343a40}#download-column{padding-top:2rem}#download-column #download-content{padding-bottom:3.25rem}#download-column #download-content #download-details{position:relative;min-height:400px;padding:2.2em 3.3em 1.6em}#download-column #download-content #download-details section#addresses{color:#6c757d}#download-column #download-content #download-details section#addresses.full-info{padding-top:1.2em}#download-column #download-content #download-details section#custom-fields #cf-tablewrap{width:600px;max-width:100%;margin:0 auto}#download-column #download-content #download-details section#custom-fields #cf-tablewrap table{width:100%}#download-column #download-content #download-details section#custom-fields #cf-tablewrap table td{width:50%}#download-column #download-content #download-details section#custom-fields .cf-label{text-align:right;padding-right:5px}#download-column #download-content #download-details section#custom-fields .cf-value{font-weight:700;white-space:pre-wrap}#download-column #download-content #download-details section#download-buttons{padding:30px 0;text-align:center}#download-column #download-content #download-details section#download-buttons #buttons-wrap{width:100%;text-align:center}#download-column #download-content #download-details section#download-buttons #buttons-wrap .btn{min-width:220px}#download-column #download-content #download-details section#download-buttons #buttons-wrap .btn.btn-lg{padding-left:1.75rem;padding-right:1.75rem}#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor{font-size:.95rem}#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor .fake-link,#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor a{color:#6c757d!important;cursor:pointer}#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor .fake-link:hover,#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor a:hover{color:#545b62!important;text-decoration:underline}#download-column #download-content #download-details section#download-buttons #buttons-wrap .minor .share-link{word-break:break-word}#download-column #download-content #download-details section#message{margin-top:1.5em;white-space:pre-wrap}#download-column #download-content #download-details section#files{padding-top:20px}#download-column #download-content #download-details section#files .plus{padding-top:5px}#download-column #download-content #download-details section#files .listwrap table{margin:0 auto}#download-column #download-content #download-details section#files .listwrap td{font-size:.85em}#download-column #download-content #download-details section#files .listwrap td .size{color:#adb5bd}#download-column #download-content #download-details section#files #thumbwrap .plus{margin-top:20px;text-align:center}#download-column #download-content #download-details section#files #thumbwrap .thumblist{margin:0 -20px 0 0}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap{position:absolute;top:0;left:-9999px;height:auto;margin:0;border:none;margin-bottom:25px;width:calc(25% - 20px)}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .info{text-align:center;font-size:.9rem;line-height:16px;word-wrap:break-word}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .info.minor{word-break:break-all;word-wrap:normal}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .info a{display:block}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .minor{color:#6c757d}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap img{display:block;width:100%;height:auto}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .bg-tile{display:block;background-color:#e9ecef;color:#ddd;text-align:center;height:auto;border:1px solid #e9ecef;margin-bottom:4px}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .bg-tile .img-icon{color:#cbd3da;font-size:26px}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .bg-tile .err-icon{color:#ffc107;font-size:26px;display:none}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap.loaded-err .bg-tile{height:150px;line-height:150px}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap.loaded-err .bg-tile .err-icon{display:inline-block}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .video-toolbar{position:absolute;top:5px;right:5px}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .video-toolbar>i{background-color:#fff;color:#1377c3;border:1px solid #1377c3;border-radius:3px;padding:3px;vertical-align:middle}#download-column #download-content #download-details section#files #thumbwrap .thumblist .imgwrap .video-toolbar .video-play{display:inline-block;cursor:pointer;width:30px}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-3 .thumblist{margin:0 auto;width:75%}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-3 .imgwrap{width:calc(33.333% - 20px);margin-left:10px;margin-right:10px}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-2 .thumblist{margin:0 auto;width:50%}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-2 .imgwrap{width:calc(50% - 20px);margin-left:10px;margin-right:10px}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-1 .thumblist{margin:0 auto;width:25%}#download-column #download-content #download-details section#files #thumbwrap.thumbwrap-1 .imgwrap{width:100%}#download-column #download-content #download-details section#files .minor{font-size:.9em}#download-column #download-content #download-details section#files .file-loader{text-align:center;padding:20px 0 0}#download-column #download-content #download-details .minor{color:#6c757d}#download-column #download-content #download-details .error-message{text-align:center;font-size:1.3rem;line-height:1.5rem;padding-top:120px}#download-column #download-content #download-details .error-message .fa-exclamation-triangle{color:#dc3545}#download-column #download-content #download-details .expire-message{padding-top:50px}#download-column #download-content #download-details .expire-message .left{float:left;padding-top:22px;width:150px}#download-column #download-content #download-details .expire-message .right{padding-left:150px}#download-column #download-content #download-details .transfer-login{padding-top:50px;text-align:center}#download-column #download-content #download-details .transfer-login input[type=text]{width:300px;max-width:100%;padding:8px}#download-column #download-content #download-details .transfer-login input[type=submit]{border:none}#download-column #download-content #download-details .transfer-login img{max-width:180px}#download-column #download-content #download-details .loader.big{text-align:center;margin:100px 0}#download-column #download-content #download-details .separated{border-bottom:1px solid #e6e6e6;padding:1.5em 0}#download-column #download-content #download-details .separated:first-child{padding-top:0}#download-column #download-content #download-details .separated:last-child{border:none;padding-bottom:0}#download-column #download-content #download-footer{margin:20px 0;text-align:center;color:#6c757d}#download-column #download-content #download-footer a,#download-column #download-content #download-footer a:hover{color:#6c757d!important}#download-column #download-content #download-footer a:hover{text-decoration:underline;color:#545b62!important}#download-column #download-content #download-footer .powered-by{font-size:.75em!important;color:#999!important}#download-column #download-content #download-footer .powered-by a#powered-by-link{color:#999!important}#logoHolder{width:100%;background-color:#f8f9fa;padding:0;position:relative;top:0}#logoHolder .container .img-wrap{float:left;min-height:60px;padding:11px 0}#logoHolder .container img{max-height:38px;max-width:300px}#logoHolder .container .navigation-outer{float:right;width:auto;padding:15px 0}.wait-icon{cursor:wait!important}.ftp-info-popup{width:100%;max-width:800px}.ftp-info-popup .clipper{color:#1377c3;cursor:pointer}@media only screen and (max-width:768px){.ftp-info-popup{max-width:100%}.ftp-info-popup .left{display:none}.ftp-info-popup .rightpane{padding-left:0}#download-column{padding-top:1rem}#download-column #download-content #download-details{padding:1.3em 2.2em}.thumbwrap-1 .thumblist{width:50%!important}.thumbwrap-2 .thumblist{width:75%!important}.thumbwrap-3 .thumblist{width:100%!important}.thumbwrap-4 .thumblist .imgwrap{width:calc(50% - 20px)!important}}@media only screen and (max-width:480px){.thumbwrap-1 .thumblist,.thumbwrap-2 .thumblist,.thumbwrap-3 .thumblist,.thumbwrap-4 .thumblist{width:100%!important}.thumbwrap-1 .thumblist .imgwrap,.thumbwrap-2 .thumblist .imgwrap,.thumbwrap-3 .thumblist .imgwrap,.thumbwrap-4 .thumblist .imgwrap{width:calc(50% - 20px)!important;width:100%!important;margin-right:0!important;margin-left:0!important}}.mac-tip{padding:30px;text-align:center}.desktop-launcher{text-align:center}div.tooltip-inner{max-width:800px!important;text-align:left}.button,.button:hover{border-color:transparent;border-width:0}.mobile-popup-drop{font-size:1.1em;background-color:rgba(52,58,64,.5);position:absolute;width:100%;min-height:100%;z-index:5000}.mobile-popup-drop .mobile-popup{width:91vw;max-width:500px;margin:2em auto 6em}.mobile-popup-drop .mobile-popup .mobile-button,.mobile-popup-drop .mobile-popup .mobile-popup-section{background-color:#fff;border-radius:1em;border:1px solid #eee;line-height:1.2em}.mobile-popup-drop .mobile-popup .mobile-popup-section{padding:1.5em}.mobile-popup-drop .mobile-popup .mobile-button{padding:1em;margin-top:.7em;text-align:center;color:#1377c3;cursor:pointer}.mobile-popup-drop .mobile-popup .mobile-button:active{background-color:#f8f9fa}.mobile-popup-drop .mobile-popup .mobile-button.btn-minor{color:#6c757d;font-size:.9em}.mobile-popup-drop .mobile-popup .pictures{display:flex;flex-direction:row;justify-content:space-between}.mobile-popup-drop .mobile-popup .source-col{display:flex;align-items:center;justify-content:center}.mobile-popup-drop .mobile-popup .source-col img{max-width:90%;max-height:100px;margin-top:-10px}.mobile-popup-drop .mobile-popup .target-row{text-align:center;display:flex;flex-direction:row;justify-content:space-around}.mobile-popup-drop .mobile-popup .target-row>div,.mobile-popup-drop .mobile-popup .target-row>svg{align-self:center}.mobile-popup-drop .mobile-popup .target-row>div{width:40%}.mobile-popup-drop .mobile-popup .target-row svg{width:30%;height:40px}.mobile-popup-drop .mobile-popup .target-row img{width:90%}.mobile-popup-drop .mobile-popup .target-row .pic-sub{font-size:.7em;margin-top:5px}body.mobile-view #app-holder{position:fixed;width:100%}.mobile-open-in-app{font-size:.8em;cursor:pointer;position:fixed;bottom:10px;padding:.5em 1em;border-radius:10px;color:#fff;background-color:#1377c3;z-index:100;margin:0 auto;left:50%;transform:translateX(-50%);min-width:200px}.mobile-open-in-app .closebtn{color:#fff;margin-left:15px;font-size:1.25em;vertical-align:middle}
#background_cycler{background-color:#eee;padding:0;margin:0;position:fixed;top:0;left:0;bottom:0;right:0;z-index:-1}#background_cycler div{position:absolute;left:0;top:0;bottom:0;right:0;background-size:cover;opacity:0;transition-delay:2s;background-repeat:no-repeat}#background_cycler div.active{opacity:1;transition:opacity 2s ease-in-out}#background_cycler .zoomIn{transition:all 30s ease!important;width:110%;height:1300px}#background_cycler .copyright{position:absolute;top:0;left:-9999px}#background_cycler .bgImages{background-position:center center}</style>

    <link rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" type="text/css" href="/bundle/css/bluemaster-later/0d2fa83d37fdcda" />

    <script>!function (t) { "use strict"; t.loadCSS || (t.loadCSS = function () { }); var e = loadCSS.relpreload = {}; if (e.support = function () { var e; try { e = t.document.createElement("link").relList.supports("preload") } catch (t) { e = !1 } return function () { return e } }(), e.bindMediaToggle = function (t) { var e = t.media || "all"; function a() { t.addEventListener ? t.removeEventListener("load", a) : t.attachEvent && t.detachEvent("onload", a), t.setAttribute("onload", null), t.media = e } t.addEventListener ? t.addEventListener("load", a) : t.attachEvent && t.attachEvent("onload", a), setTimeout(function () { t.rel = "stylesheet", t.media = "only x" }), setTimeout(a, 3e3) }, e.poly = function () { if (!e.support()) for (var a = t.document.getElementsByTagName("link"), n = 0; n < a.length; n++) { var o = a[n]; "preload" !== o.rel || "style" !== o.getAttribute("as") || o.getAttribute("data-loadcss") || (o.setAttribute("data-loadcss", !0), e.bindMediaToggle(o)) } }, !e.support()) { e.poly(); var a = t.setInterval(e.poly, 500); t.addEventListener ? t.addEventListener("load", function () { e.poly(), t.clearInterval(a) }) : t.attachEvent && t.attachEvent("onload", function () { e.poly(), t.clearInterval(a) }) } "undefined" != typeof exports ? exports.loadCSS = loadCSS : t.loadCSS = loadCSS }("undefined" != typeof global ? global : this);</script>
    
<style> 
    /* corp colors */
    
</style>

    
<link rel="canonical" href="https://www.filemail.com/d/dtzlqjkaktlsuza" />
<meta property="og:url" content="https://www.filemail.com/d/dtzlqjkaktlsuza" />

    
    </head>
<body>
    <form method="post" action="./dtzlqjkaktlsuza?transferId=dtzlqjkaktlsuza&amp;" id="ctl00">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="KcK0xgwBZKl7mubgrEdcQ4RQYgFT9lizGtnaVYa/7DSbaHz8swM4NvbKoKfNl4Ocgvh8N8mewAnrr6WRq5HW9COArUM=" />
</div>

<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="1FBA4199" />
</div>
        
        <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="fmNavbar">
            <div class="container">
                

<a class="navbar-brand" href="/">
    <img id="imgLogo" src="/images/logo/logo-horiz.svg" class="navbar-logo standard-logo d-none d-sm-block" alt="Filemail Logo" width="174" height="40" />
    <img id="imgLogoMobile" src="/images/logo/logo.svg" class="navbar-logo standard-logo d-block d-sm-none" alt="Filemail Logo" width="55" height="40" />
</a>
<div id="navbar-right">
    
    <a href="/price-plans-comparison" class="btn btn-outline-secondary ml-auto d-lg-none d-inline-block mr-2 goto-plans">
        Sign up
    </a>
    
    <a href="/login" class="btn btn-outline-primary ml-auto d-lg-none d-inline-block mr-2">
        Log in
    </a>
    <button class="navbar-toggler collapsed" aria-label="Filemail menu button" type="button" data-toggle="collapse" data-target="#fmNavbarToggle">
        <span class="navbar-toggler-icon"></span>
    </button>
</div>
<div id="fmNavbarToggle" class="navbar-collapse collapse">
    <ul class="navbar-nav">

        <li class="nav-item foldable" data-unfold="solutions">
            
            <span class="nav-link">
                Solutions
                <i class="ml-0 ml-lg-1 fas fa-chevron-down"></i>
                <i class="ml-0 ml-lg-1 fas fa-chevron-up"></i>
            </span>
            
            <div class="mega-menu" id="mega-menu-solutions">
                <div class="mega-menu-content nowrap">
                    <div class="mega-menu-col">
                        <p class="d-none d-lg-block ">File transfer apps</p>
                        <ul>
                            <li><a href="https://www.filemail.com/content/apps/android-file-transfer-app/">Android</a></li>
                            <li><a href="/apps/file-sharing-api">API</a></li>
                            <li><a href="/apps/iphone">iPhone</a></li>
                            <li><a href="/apps/outlook-add-in-to-send-large-files">Outlook</a></li>
                            <li><a href="/apps/mac">Mac</a></li>
                            <li><a href="/apps/windows">Windows</a></li>
                            <li><a href="/apps/linux">Linux</a></li>
                        </ul>
                    </div>
                    <div class="mega-menu-col">
                        <p>Products</p>
                        <ul>
                            <li><a href="/pro">Pro</a></li>
                            <li><a href="/business">Business</a></li>
                            <li><a href="/enterprise-managed-file-transfer-mft">Enterprise MFT</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </li>
        <li class="nav-item foldable" data-unfold="features">
            
            <span class="nav-link">
                Features
                <i class="ml-0 ml-lg-1 fas fa-chevron-down"></i>
                <i class="ml-0 ml-lg-1 fas fa-chevron-up"></i>
            </span>
            
            <div class="mega-menu fullwidth" id="mega-menu-features">
                <div class="mega-menu-content">
                    <div class="mega-menu-col">
                        <p>Share</p>
                        <ul>
                            <li><a href="/share/automatic-download">Automatic Download</a></li>
                            <li><a href="/share/download-files-any-way-you-like">Download files</a></li>
                            <li><a href="/share/filemail-apis">Filemail API</a></li>
                            <li><a href="https://www.filemail.com/content/share/file-request/">File request</a></li>
                            <li><a href="/share/keep-track-of-files-and-people">File tracking</a></li>
                            <li><a href="/share/link-sharing">Link Sharing</a></li>
                            <li><a href="https://www.filemail.com/content/share/receive-large-files/">Receive large files</a></li>
                            <li><a href="https://www.filemail.com/content/share/udp-transfer-acceleration/">UDP Transfer Acceleration</a></li>
                            <li><a href="/share/upload-file">Upload files</a></li>
                            <li><a href="/share/upload-form-integration">Upload form integration</a></li>
                            <li><a href="/share/upload-images">Upload Images</a></li>
                        </ul>
                    </div>
                    <div class="mega-menu-col">
                        <p>Customize</p>
                        <ul>
                            <li><a href="/customize/customization-and-branding">Customization And Branding</a></li>
                            <li><a href="/customize/custom-subdomain">Custom Subdomain</a></li>
                        </ul>
                    </div>
                    <div class="mega-menu-col">
                        <p>MFT Features</p>
                        <ul>
                            <li><a href="/mft-features/full-audit-trail-and-governance">Full audit trail and governance</a></li>
                            <li><a href="https://www.filemail.com/content/mft-features/hipaa-compliant-file-sharing/">HIPAA compliant file sharing</a></li>
                            <li><a href="/mft-features/pentest-report-access">Pentest report access</a></li>
                            <li><a href="/mft-features/saml-sso">SAML/SSO</a></li>
                            <li><a href="/mft-features/two-factor-authentication">Two factor authentication</a></li>
                        </ul>
                    </div>
                    <div class="mega-menu-col">
                        <p>Security</p>
                        <ul>
                            <li><a href="/security/secure-data-transfer-and-storage">Secure data transfer and storage</a></li>
                            <li><a href="/security/gdpr">GDPR</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </li>
    </ul>
    <ul class="navbar-nav ml-auto">
        <li class="nav-item">
            <a class="nav-link" target="_blank" href="https://www.filemail.com/content/filemail-affiliate-program/" rel="noopener nofollow">
                Affiliate program
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://www.filemail.com/blog" rel="noopener">
                Blog
            </a>
        </li>
        <li class="nav-item foldable" data-unfold="help">
            <div class="nav-link">
                Help
                <i class="ml-0 ml-lg-1 fas fa-fw fa-chevron-down"></i>
                <i class="ml-0 ml-lg-1 fas fa-chevron-up"></i>
            </div>
            <div class="mega-menu" id="mega-menu-help">
                <div class="mega-menu-content nowrap p-0">
                    <div class="mega-menu-col py-2 px-0">
                        <a class="dropdown-item" href="https://support.filemail.com"><i class="fal fa-fw fa-comments-alt"></i>Support</a>
                        <a class="dropdown-item" href="/how-to-send-large-files"><i class="fal fa-fw fa-shipping-fast"></i>How to send large files</a>
                    </div>
                </div>
            </div>
        </li>

        
        <li class="nav-item d-none d-lg-block">
            <a href="/price-plans-comparison" class="btn btn-outline-secondary goto-plans" rel="nofollow">
                Sign up
            </a>
        </li>
        
        <li id="loginNav" class="nav-item d-none d-lg-block">
            <a href="/login" class="btn btn-outline-primary" rel="nofollow">
                Log in
            </a>
        </li>
    </ul>
</div>

                
            </div>
        </nav>
        
    
<div id="background_cycler" >
    
        <div data-bgimage="/Frontend/images/backgrounds/122.jpg" style="background-image: url('/Frontend/images/backgrounds/122.jpg');" class="bgImages retina-img active img-set"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/069.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/131.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/153.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/041.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/024.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/066.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/165.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/161.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/077.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/119.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/099.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/053.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/110.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/094.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/098.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/072.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/145.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/144.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/176.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/030.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/027.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/065.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/105.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/120.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/147.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/089.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/075.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/049.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/158.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/044.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/085.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/020.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/025.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/091.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/168.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/100.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/064.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/071.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/040.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/164.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/062.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/045.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/167.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/015.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/125.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/093.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/173.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/146.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/043.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/097.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/076.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/126.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/140.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/087.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/009.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/151.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/137.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/050.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/022.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/114.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/124.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/130.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/055.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/032.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/107.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/012.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/011.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/070.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/178.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/155.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/008.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/034.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/143.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/103.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/048.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/123.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/175.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/026.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/061.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/128.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/152.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/063.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/060.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/033.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/035.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/014.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/109.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/080.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/047.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/073.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/039.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/115.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/170.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/006.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/074.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/171.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/068.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/108.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/157.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/149.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/139.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/117.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/159.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/054.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/169.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/177.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/083.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/002.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/037.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/082.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/084.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/135.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/141.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/046.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/042.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/111.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/058.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/134.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/166.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/019.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/057.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/003.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/142.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/056.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/028.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/090.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/133.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/059.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/095.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/172.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/163.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/129.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/116.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/104.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/078.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/118.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/121.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/156.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/016.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/174.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/101.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/031.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/052.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/138.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/096.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/113.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/079.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/160.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/127.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/036.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/088.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/067.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/005.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/162.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/004.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/106.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/010.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/023.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/013.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/021.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/007.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/112.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/029.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/148.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/092.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/051.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/038.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/081.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/154.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/102.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/150.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/001.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/132.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/136.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/018.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/086.jpg" class="bgImages retina-img"></div>
    
    <div data-bgimage="/Frontend/images/backgrounds/017.jpg" class="bgImages retina-img"></div>
    
    <span class="copyright">Photos by Unsplash</span>
    
</div>



        

    <div id="app-holder">
        <div id="logoHolder" class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <div class="img-wrap">
                    
                    <h3>
                        Longfen1760
                    </h3>
                    
                </div>
                
            </div>
        </div>
        
        <div id="download-column" class="container" ng-app="filemail.download">
            
            <div id="download-content">
                <div id="download-details" class="whiteHolder">
                    <download-details config="{ 
                            transferId: 'dtzlqjkaktlsuza',
                            trackId: null,
                            ftpUsername: 'dtzlqjkaktlsuza',
                            skipDownloadRegistration: false,
                            passwordRequired: false,

                            captchaRequired: false,
                            status: 'STATUS_COMPLETE',
                            notFound: false,

                            transferExpired: null,
                            corpExpired: null,
                            corpExpiredMode: null,
                            showAllRecipients: false,
                            display: { ftp: true,
                                       torrent: true, 
                                       sharinglink: true, 
                                       showMD5: false,
                                       maxFiles: -1,
                                       showThumbs: true,
                                       showFilesBelowThumbs: true
                                     }
                        }"></download-details>
                </div>
                <div id="download-footer" class="whiteHolder p-3">
                    
                            <p>Longfen1760</p>
                        
                    <div class="text-center powered-by">
                        <a id="powered-by-link" href="https://www.filemail.com">Send Files With Filemail</a>
                    </div>
                </div>
            </div>
            
        </div>
        
    </div>
    
        <div class="mobile-open-in-app btn btn-primary" onclick="Filemail.branchDVC()" style="display: none">
            Open the Filemail app<i class="fal fa-times closebtn"></i>
        </div>
    

        </form>

    

    
<script>
    !function(e){var t=e.Filemail=e.Filemail||{};t.recaptcha={},t.recaptcha.setup=function(i){this.sitekey=i,this.initDone=!1,t.recaptcha.getToken=function(t){t=t||"submit";var i=this,n=new $.Deferred;return this.init().then((function(){e.grecaptcha.execute(i.sitekey,{action:t}).then((function(e){n.resolve(e)}))})),n.promise()},t.recaptcha.init=function(){var i=this,n=new $.Deferred;if(i.initDone)n.resolve();else{e.__recaptchaCallback=function(){i.initDone=!0,n.resolve()};var a="https://www.google.com/recaptcha/api.js?render="+i.sitekey+"&onload=__recaptchaCallback";t.loadScript(a,null,{async:!0})}return n.promise()}}}(window);

    Filemail.recaptcha.setup('6LfiE5ocAAAAAPIxSggV1OLpAwQcnEJPbS7aqwNp');
</script>

    
    <script src="/bundle/js/common_master-bluemaster_common-anonymous_downloadslim-downloadslim/7d083f6eeecfea47cd03e17aa417f17ea7cf4cff0841033005b9d15ef1c5"></script>

    

    
    
    <script>
         
    </script>
    <script>
        (function () {
            var payload = {
                mobile: Filemail.OSdetect === 'iOS' || Filemail.OSdetect === 'Android',
                mobileOS: Filemail.OSdetect.toLowerCase()
            };
            $.extend(payload, JSON.parse(Filemail.b64decode('eyJtb2JpbGVEb3dubG9hZEFsbG93ZWQiOnRydWUsImludGVncmF0ZWQiOmZhbHNlLCJzaG93Q29uZmlybWF0aW9uIjpmYWxzZSwic2tpcERvd25sb2FkUmVnaXN0cmF0aW9uIjpmYWxzZSwid2lkZ2V0SWQiOm51bGx9')));
            new Filemail.pages.downloadSlim(payload);
        })();
    </script>
    


    
<script>
    (function (w, d) {
        var l = function () {
            w.intercomSettings = JSON.parse(Filemail.b64decode('eyJhcHBfaWQiOiJwNDFyMThveCIsImlwIjoiODQuMTkyLjUxLjExMSJ9'));
            var ic = w.Intercom;
            if (typeof ic === "function") {
                ic('reattach_activator');
                ic('update', intercomSettings);
            } else {
                var i = function () {
                    i.c(arguments);
                };
                i.q = [];
                i.c = function (args) {
                    i.q.push(args);
                };
                w.Intercom = i;
                var s = d.createElement('script');
                s.type = 'text/javascript';
                s.async = true;
                s.src = 'https://widget.intercom.io/widget/p41r18ox';
                var x = d.getElementsByTagName('script')[0];
                x.parentNode.insertBefore(s, x);
            }
        };
        
        var x = function () {
            setTimeout(l, 6002);
        };
        if (w.attachEvent) {
            w.attachEvent('onload', x);
        } else {
            w.addEventListener('load', x, false);
        }
        
        })(window, document);
</script>

    
    

</body>
</html>
