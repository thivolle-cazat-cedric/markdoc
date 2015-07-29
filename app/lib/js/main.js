$(document).ready(function() {
  	$('[data-toggle="tooltip"]').tooltip()
  	$('pre code').each(function(i, block) {
  		$('pre code').parent().addClass('hljs');
	    hljs.highlightBlock(block);
	  });

});