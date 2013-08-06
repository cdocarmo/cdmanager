$(document).on("ready", inicio);
function inicio ()
{

	
}

function cambiarActive (datos) 
{
	var col = datos.currentTarget.id;
	$("#" + col).attr("class", "active");
}
function buscarArticulos (datos) 
{

	var col = $('#text-art').val();
	col = col.replace(" ","-");
	
	$('#articulos').html('&nbsp;').load($get('articulos/search/?q=' + col));	
	alert(col);
}