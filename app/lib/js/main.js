$(document).ready(function() {
  	$('[data-toggle="tooltip"]').tooltip()
  	$('pre code').each(function(i, block) {
  		$(this).parent().addClass('hljs');
	    hljs.highlightBlock(block);
	  });
	
	$('.lang-exemple').each(function(i) {
		console.log(this)
	    $(this).parent().removeClass('hljs');
	 });

});