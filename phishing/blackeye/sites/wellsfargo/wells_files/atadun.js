var ndURI = ndURI || '';
var isNative = isNative || false;

(function(ndURI, isNative) {
    if(!isNative){
        if(ndURI === '') {
            ndURI = 'https://connect.secure.wellsfargo.com/ATADUN/2.2/w/w-642409/sync/js/';
        }
        if(ndURI !== '') {
        	var baseUrl = ndURI;
        	var idx = baseUrl.indexOf("/ATADUN");
        	var jsURI = baseUrl.substring(0,idx);
       	
        	nds=window.ndsapi||(window.ndsapi={});
        	nds.config={q:[],ready:function(cb){this.q.push(cb)}};
        	nds.config.ready(function() {
        		// Set Placement as Login
        		nds.setPlacement('Login');
        		// Bind to the submit button on the page
        		nds.sendOnSubmit();
        	});
        	
        	js = document.createElement("script");
        	fjs = document.getElementsByTagName("script")[0];
        	js.src = jsURI + "/jenny/nd";
        	fjs.parentNode.insertBefore(js,fjs);
        	js.onload=function(){
        		nds.load(baseUrl);
        	}        	
        }
    }
} (ndURI, isNative));
