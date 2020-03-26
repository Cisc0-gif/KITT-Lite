//Drop Down Tabs Menu- Author: Dynamic Drive (http://www.dynamicdrive.com)
//Created: May 16th, 07'

var tabdropdown={
	disappeardelay: 200, //set delay in miliseconds before menu disappears onmouseout
	disablemenuclick: false, //when user clicks on a menu item with a drop down menu, disable menu item's link?
	enableiframeshim: 1, //1 or 0, for true or false

	//No need to edit beyond here////////////////////////
	dropmenuobj: null, ie: document.all, firefox: document.getElementById&&!document.all, previousmenuitem:null,
	currentpageurl: window.location.href.replace("http://"+window.location.hostname, "").replace(/^\//, ""), //get current page url (minus hostname, ie: http://www.dynamicdrive.com/)

	getposOffset:function(what, offsettype){
		var totaloffset=(offsettype=="left")? what.offsetLeft : what.offsetTop;
		var parentEl=what.offsetParent;
			while (parentEl!=null){
				totaloffset=(offsettype=="left")? totaloffset+parentEl.offsetLeft : totaloffset+parentEl.offsetTop;
				parentEl=parentEl.offsetParent;
			}
		return totaloffset;
	},

	showhide:function(obj, e, obj2){ //obj refers to drop down menu, obj2 refers to tab menu item mouse is currently over
		if (this.ie || this.firefox)
			this.dropmenuobj.style.left=this.dropmenuobj.style.top="-500px"
		if (e.type=="click" && obj.visibility==hidden || e.type=="mouseover"){
			if (obj2.parentNode.className.indexOf("default")==-1) //if tab isn't a default selected one
				obj2.parentNode.className="selected"
			obj.visibility="visible"
			}
		else if (e.type=="click")
			obj.visibility="hidden"
	},

	iecompattest:function(){
		return (document.compatMode && document.compatMode!="BackCompat")? document.documentElement : document.body
	},

	clearbrowseredge:function(obj, whichedge){
		var edgeoffset=0
		if (whichedge=="rightedge"){
			var windowedge=this.ie && !window.opera? this.standardbody.scrollLeft+this.standardbody.clientWidth-15 : window.pageXOffset+window.innerWidth-15
			this.dropmenuobj.contentmeasure=this.dropmenuobj.offsetWidth
		if (windowedge-this.dropmenuobj.x < this.dropmenuobj.contentmeasure)  //move menu to the left?
			edgeoffset=this.dropmenuobj.contentmeasure-obj.offsetWidth
		}
		else{
			var topedge=this.ie && !window.opera? this.standardbody.scrollTop : window.pageYOffset
			var windowedge=this.ie && !window.opera? this.standardbody.scrollTop+this.standardbody.clientHeight-15 : window.pageYOffset+window.innerHeight-18
			this.dropmenuobj.contentmeasure=this.dropmenuobj.offsetHeight
			if (windowedge-this.dropmenuobj.y < this.dropmenuobj.contentmeasure){ //move up?
				edgeoffset=this.dropmenuobj.contentmeasure+obj.offsetHeight
				if ((this.dropmenuobj.y-topedge)<this.dropmenuobj.contentmeasure) //up no good either?
					edgeoffset=this.dropmenuobj.y+obj.offsetHeight-topedge
			}
			this.dropmenuobj.firstlink.style.borderTopWidth=(edgeoffset==0)? 0 : "1px" //Add 1px top border to menu if dropping up
		}
		return edgeoffset
	},

	dropit:function(obj, e, dropmenuID){
		if (this.dropmenuobj!=null){ //hide previous menu
			this.dropmenuobj.style.visibility="hidden" //hide menu
			if (this.previousmenuitem!=null && this.previousmenuitem!=obj){
				if (this.previousmenuitem.parentNode.className.indexOf("default")==-1) //If the tab isn't a default selected one
					this.previousmenuitem.parentNode.className=""
			}
		}
		this.clearhidemenu()
		if (this.ie||this.firefox){
			obj.onmouseout=function(){tabdropdown.delayhidemenu(obj)}
			this.dropmenuobj=document.getElementById(dropmenuID)
			this.dropmenuobj.onmouseover=function(){tabdropdown.clearhidemenu()}
			this.dropmenuobj.onmouseout=function(e){tabdropdown.dynamichide(e, obj)}
			this.showhide(this.dropmenuobj.style, e, obj)
			this.dropmenuobj.x=this.getposOffset(obj, "left")
			this.dropmenuobj.y=this.getposOffset(obj, "top")
			this.dropmenuobj.style.left=this.dropmenuobj.x-this.clearbrowseredge(obj, "rightedge")+"px"
			this.dropmenuobj.style.top=this.dropmenuobj.y-this.clearbrowseredge(obj, "bottomedge")+obj.offsetHeight+1+"px"
			this.previousmenuitem=obj //remember main menu item mouse moved out from (and into current menu item)
			this.positionshim() //call iframe shim function
		}
	},

	contains_firefox:function(a, b) {
		while (b.parentNode)
		if ((b = b.parentNode) == a)
			return true;
		return false;
	},

	dynamichide:function(e, obj2){ //obj2 refers to tab menu item mouse is currently over
		var evtobj=window.event? window.event : e
		if (this.ie&&!this.dropmenuobj.contains(evtobj.toElement))
			this.delayhidemenu(obj2)
		else if (this.firefox&&e.currentTarget!= evtobj.relatedTarget&& !this.contains_firefox(evtobj.currentTarget, evtobj.relatedTarget))
			this.delayhidemenu(obj2)
	},

	delayhidemenu:function(obj2){
		this.delayhide=setTimeout(function(){tabdropdown.dropmenuobj.style.visibility='hidden'; if (obj2.parentNode.className.indexOf('default')==-1) obj2.parentNode.className=''},this.disappeardelay) //hide menu
	},

	clearhidemenu:function(){
		if (this.delayhide!="undefined")
			clearTimeout(this.delayhide)
	},

	positionshim:function(){ //display iframe shim function
		if (this.enableiframeshim && typeof this.shimobject!="undefined"){
			if (this.dropmenuobj.style.visibility=="visible"){
				this.shimobject.style.width=this.dropmenuobj.offsetWidth+"px"
				this.shimobject.style.height=this.dropmenuobj.offsetHeight+"px"
				this.shimobject.style.left=this.dropmenuobj.style.left
				this.shimobject.style.top=this.dropmenuobj.style.top
			}
		this.shimobject.style.display=(this.dropmenuobj.style.visibility=="visible")? "block" : "none"
		}
	},

	hideshim:function(){
		if (this.enableiframeshim && typeof this.shimobject!="undefined")
			this.shimobject.style.display='none'
	},

isSelected:function(menuurl){
	var menuurl=menuurl.replace("http://"+menuurl.hostname, "").replace(/^\//, "")
	return (tabdropdown.currentpageurl==menuurl)
},

	init:function(menuid, dselected){
		this.standardbody=(document.compatMode=="CSS1Compat")? document.documentElement : document.body //create reference to common "body" across doctypes
		if ( document.getElementById(menuid) != null )
		{
            var menuitems=document.getElementById(menuid).getElementsByTagName("a")
            for (var i=0; i<menuitems.length; i++){
                if (menuitems[i].getAttribute("rel")){
                    var relvalue=menuitems[i].getAttribute("rel")
                    document.getElementById(relvalue).firstlink=document.getElementById(relvalue).getElementsByTagName("a")[0]
                    menuitems[i].onmouseover=function(e){
                        var event=typeof e!="undefined"? e : window.event
                        tabdropdown.dropit(this, event, this.getAttribute("rel"))
                    }
                }
                if (dselected=="auto" && typeof setalready=="undefined" && this.isSelected(menuitems[i].href)){
                    menuitems[i].parentNode.className+=" selected default"
                    var setalready=true
                }
                else if (parseInt(dselected)==i)
                    menuitems[i].parentNode.className+=" selected default"
            }
        }
	}

}
function forward(url)
{
    hideSpreadSheet();
    jQuery('#forward').attr('value',url);
    jQuery('#event_override').attr('value','forward');
    jQuery('#form').data("passThrough","true"); // if embedded in another page, let event be handled normally because we are leaving page


    jQuery('#form').submit();
};


function showSpreadSheet()
{
    var progress = document.getElementById('spreadsheet_form');
    if (progress != null)
    {
        progress.style.visibility = 'visible';
    }
    return true;
}

function hideSpreadSheet()
{
    var progress = document.getElementById('spreadsheet_form');
    if (progress != null)
    {
        progress.style.visibility = 'hidden';
    }
    return true;
}

function confirm_delete(message, destination)
{
    if ( confirm(message) )
    {
        window.location=destination;
    }
}

function extractID(prefix, divID)
{
    var result = null;
    if ( divID.indexOf(prefix) == 0 )
    {
        result = divID.substring(prefix.length);
    }
    return result;
}

function submit_sort(sort_key)
{
    var selector = "#form > #sort";
    jQuery(selector).attr('value', sort_key);
    submit_event('sort');
}

function submit_sort_form(formID, sort_key)
{
    var selector = formID + " > " + formID + "_sort"; 
    jQuery(selector).attr('value', sort_key);
    submit_event_form(formID, 'sort');
}

function submit_page_items_form(formID, value)
{
    var selector = formID + " > #page_item_count";
    jQuery(selector).attr('value', value);
    submit_event_form(formID, 'page_item_count');
}

function submit_page_index_form(formID, pageIndex)
{
    var selector = formID + " > " + formID + "_page_index"; 
    jQuery(selector).attr('value', pageIndex);
    submit_event_form(formID, 'page_index');
}

function submit_reverse(isReversed)
{
    var selector = "#reverse";
    jQuery(selector).attr('value',isReversed);
    submit_even('reverse');
}

function submit_reverse_form(formID, isReversed)
{
    var selector = "#form_reverse";
    jQuery(selector).attr('value',isReversed);
    submit_event_form(formID, 'reverse');
}

function submit_event(event)
{
    submit_event_form('#form', event);
}

function submit_event_form(formID, event)
{
var target = jQuery(formID);
jQuery("#event_override", target).val(event);
jQuery(formID).submit();
}

function goto(url)
{
    window.location = url;
}

function getUrlVars()
{
    var vars = {}, hash;
    var index = window.location.href.indexOf('?');
    if(index >= 0) {
        var hashes = window.location.href.slice(index + 1).split('&');
        for(var i = 0; i < hashes.length; i++)
        {
            hash = hashes[i].split('=');
            vars[hash[0]] = hash[1];
        }
    }
    return vars;
}

function select_checkboxes(checkboxes, state)
{
    if(checkboxes.length) {
        for(var i=0; i < checkboxes.length; i++) {
            checkboxes[i].checked=state;
        }
    } else {
        checkboxes.checked=state;
    }
}

function toggle_field(showClass, hideClass, focusClass)
{
    jQuery("." + showClass).removeClass(showClass)
    jQuery("." + hideClass).css("display", "none");
    jQuery(".pipe").css("display", "none");   
    jQuery("#" + focusClass).parent().find("input").focus();
}

function toggleDiv(name)
{
    var theDiv = document.getElementById(name);
    if (theDiv != undefined)
    {
        if ( theDiv.style.display == 'block' )
        {
            theDiv.style.display = 'none';
        }
        else
        {
            theDiv.style.display = 'block';
        }
    }
    return true;
}

function addLoadEvent(func) {
    var oldonload = window.onload; 
    if (typeof window.onload != 'function') { 
        window.onload = func; 
    } else { 
        window.onload = function() { 
            if (oldonload) { 
                oldonload(); 
            } 
            func(); 
        }
    } 
} 

jQuery.fn.exists = function(){return jQuery(this).length>0;}

function autoSubmit() {
    jQuery(document).keydown(function(e) {
        var key = 0;
        if (e == null) {
            key = event.keyCode;
        } else {
            key = e.keyCode;
            if(key == 0) {
                key = e.which;
            }
        }
        
        switch(key) {
        case 13:
            submit_event('submit');
            return false;
            break;
        }
    });
}

function doAjaxTickle()
{
    jQuery.get("/misc/ajaxTickle");
    setTimeout("doAjaxTickle()",1000 * 60 * 5);
}

function initAjaxTickle()
{
    setTimeout("doAjaxTickle()",1000 * 60 * 5);
}


function setGbDrop() {

}