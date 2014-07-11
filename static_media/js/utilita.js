    var beaches = [
    ['Bondi Beach1', -31.3903665 -57.9625362, 7],
    ['Bondi Beach2', -31.3740996 -57.9583962, 6],
    ['Bondi Beach3', -31.3805813, -57.9573592, 8],
    ['Bondi Beach4', -31.3804183, -57.9572574, 9],
	['Bondi Beach', -31.380533,  -57.9572739, 4],
	['Coogee Beach', -31.370266,  -57.9712907, 5],
	['Cronulla Beach', -31.3737903, -57.9722903, 3],
	['Manly Beach', -31.3771132, -57.9636291, 2],
	['Maroubra Beach', -31.3763573, -57.9676335, 1]
    ];


$(document).on("ready", inicio);
function inicio ()
{
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if(settings.type == "POST"){
				//console.log($('[name="csrfmiddlewaretoken"]').val());
				xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
			}
		}
	});	

	$("#ver-mapa").on("click", cargo_mapa);
    $("#cargo_vv").on("click", cargo_ventasvende);

}

function cargo_detalle_pedido (argument) {
    console.log("W");
}

function cargo_ventasvende (argument) {
  var xDesde = $('#fecha_ventas_desde').val();  
  var xHasta = $('#fecha_ventas_hasta').val();
  var xVendedor = $('#vendedor-venta').val();
  var tabla = $('#tabla');




  jQuery.ajax({
    type: 'POST',
    url: "cargo_pedidovendedor/",
    data: { vendedor: xVendedor,
    fecha: xDesde, hasta: xHasta},
    dataType: 'json',

    success:  function(data) {
      var caja_cod = "";
      caja_cod = caja_cod +'<table class="table table-striped">' +

        '<thead>' +
          '<tr>' +
            '<th>Id.</th>' +
            '<th>Fecha</th>' +
            '<th>Cliente</th>' +
            '<th>Tipo</th>' +
            '<th>Total</th>' +
          '</tr>' +
        '</thead>' ;
            $.each(data.xCol, function(index, elemento){
                caja_cod = caja_cod + '<tbody id="listado-vendedor-movtos">' +
                    '<tr class="success">' +
                    
                      '<td class="id_pedido"><a href="">'+ elemento.id +'<a></td>' +
                      '<td class="nombres">'+ elemento.fecha +'</td>' +
                      '<td class="nombres">'+ elemento.cliente +'</td>' +
                      '<td class="nombres">'+ elemento.tipo +'</td>' +
                      '<td align="right" class="nombres">'+ formatNumber(elemento.total) +'</td>' +
                    '</tr>' +
                '</tbody>';
                var total 
            });
            caja_cod = caja_cod + '</table>';

            $("#movtos_vendedor").html(caja_cod);


      },
    error : function(xhr,errmsg,err) {
      $('#datos-referencia li').remove()
      console.log(xhr.status + ": " + xhr.responseText);
    }
  });
  //

}

function formatNumber(num,prefix){
    prefix = prefix || "";
    num += "";
    var splitStr = num.split('.');
    var splitLeft = splitStr[0];
    var splitRight = splitStr.length > 1 ? '.' + splitStr[1] : "";
    var regx = /(\d+)(\d{3})/;
    while (regx.test(splitLeft)) {
        splitLeft = splitLeft.replace(regx, '$1' + ',' + '$2');
    }
    return prefix + splitLeft + splitRight;
}
function unformatNumber(num) {
    return num.replace(/([^0-9\.\-])/g,"")*1;
}

function formato_numero(numero, decimales, separador_decimal, separador_miles){ // v2007-08-06
    numero=parseFloat(numero);
    if(isNaN(numero)){
        return "";
    }

    if(decimales!==undefined){
        // Redondeamos
        numero=numero.toFixed(decimales);
    }

    // Convertimos el punto en separador_decimal
    numero=numero.toString().replace(".", separador_decimal!==undefined ? separador_decimal : ",");

    if(separador_miles){
        // Añadimos los separadores de miles
        var miles=new RegExp("(-?[0-9]+)([0-9]{3})");
        while(miles.test(numero)) {
            numero=numero.replace(miles, "$1" + separador_miles + "$2");
        }
    }

    return numero;
}

$('#vendedor-gps').change(function(event){
	//console.debug($(this).val());
	//cargar_dias_gps($(this).val(), 'dias-gps');
});

function cargar_dias_gps (argument, xItem) {

	jQuery.ajax({
		type: 'POST',
		url: "fechas-vendedor/",
		data: { vendedor: argument },
		dataType: 'json',
		success:  function(data) {
			var options = '<option value="">Selecciona una ciudad</option>';
			for (var i = 0; i < data.length; i++){
		  		options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["fecha"] +'</option>'
			}
			$('#' + xItem).html(options)
			$("#"+ xItem +"option:first").attr('selected', 'selected');       

		},
		error : function(xhr,errmsg,err) {
		  $('#datos-referencia li').remove()
		  console.log(xhr.status + ": " + xhr.responseText);
		}
	});
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


function cargo_mapa (argument) {
		
	var xDia = $('#dia-gps').val();
	var xHora = $('#select-hora').val();
	var xVendedor = $('#vendedor-gps').val();


	jQuery.ajax({
		type: 'POST',
		url: "locacion-vendedor/",
		data: { vendedor: xVendedor,
		fecha: xDia,
		hora: xHora, },
		dataType: 'json',
		success:  function(data) {
			var place = new Array();
      $.each(data.xCol, function(i, elemento){
        place[i] = [i, elemento.logitud, elemento.latitud, i, elemento.cliente,
        elemento.hora, elemento.presicion, elemento.dire ];

      });
      /*
			for (var i = 0; i < data.length; i++){
        console.debug(data[i][0]);
 
    			place[i] = [
          data[i]["logitud"], data[i]["latitud"], i,
          data[i]["cliente"]];

			}
      */
      //sconsole.debug(place)
			callback(place); //AQUI
		},
		error : function(xhr,errmsg,err) {
		  $('#datos-referencia li').remove()
		  console.log(xhr.status + ": " + xhr.responseText);
		}
	});

	 function callback(response)
	    {
			var mapOptions = {
				zoom: 10,
				center: new google.maps.LatLng(-31.3876682, -57.9685929),
				mapTypeId: google.maps.MapTypeId.ROADMAP
			}
			var map = new google.maps.Map($('#map-canvas')[0],
			                            mapOptions);

			setMarkers(map, response);
      setZoom(map, response);
			infowindow = new google.maps.InfoWindow({
				content: "Loading..."
		    });	    	
	          
	    }


}

    /**
     * Data for the markers consisting of a name, a LatLng and a zIndex for
     * the order in which these markers should display on top of each
     * other.
     */




function setMarkers(map, locations) {
  // Add markers to the map
  // Marker sizes are expressed as a Size of X,Y
  // where the origin of the image (0,0) is located
  // in the top left of the image.

  // Origins, anchor positions and coordinates of the marker
  // increase in the X direction to the right and in
  // the Y direction down.

  var image_ultimo = {
    url: 'https://gmaps-samples.googlecode.com/svn/trunk/markers/green/blank.png',
    // This marker is 20 pixels wide by 32 pixels tall.
    size: new google.maps.Size(20, 32),
    // The origin for this image is 0,0.
    origin: new google.maps.Point(0,0),
    // The anchor for this image is the base of the flagpole at 0,32.
    anchor: new google.maps.Point(0, 32)
  };


  var image_inicio = {
    url: 'https://gmaps-samples.googlecode.com/svn/trunk/markers/orange/blank.png',
    // This marker is 20 pixels wide by 32 pixels tall.
    size: new google.maps.Size(20, 32),
    // The origin for this image is 0,0.
    origin: new google.maps.Point(0,0),
    // The anchor for this image is the base of the flagpole at 0,32.
    anchor: new google.maps.Point(0, 32)
  };
  



  var image = {
    url: 'https://gmaps-samples.googlecode.com/svn/trunk/markers/red/blank.png',
    // This marker is 20 pixels wide by 32 pixels tall.
    size: new google.maps.Size(20, 32),
    // The origin for this image is 0,0.
    origin: new google.maps.Point(0,0),
    // The anchor for this image is the base of the flagpole at 0,32.
    anchor: new google.maps.Point(0, 32)
  };
  // Shapes define the clickable region of the icon.
  // The type defines an HTML &lt;area&gt; element 'poly' which
  // traces out a polygon as a series of X,Y points. The final
  // coordinate closes the poly by connecting to the first
  // coordinate.
  var shape = {
      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
      type: 'poly'
  };
  for (var i = 0; i < locations.length; i++) {
    var beach = locations[i];
    var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
    image_muestra = image
    if ((locations.length -1) == i) {
    	image_muestra = image_ultimo;
    };
    if (i==0) {
    	image_muestra = image_inicio;
    };
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        icon: image_muestra,
        shape: shape,
        title: String(beach[4]),
        zIndex: beach[3],
    });
    var info = '<div id="contentInfoWindow' + beach[3]++ + '" class="contentMap">\
                        <div class="contentTxt">\
                        <h1' + String(beach[4]) + '</h1>\
                        <p>' + " ----  " + String(beach[4]) + '</p>\
                        <ul>\
                          <li> Hora.:' + String(beach[5]) + '</li>\
                          <li> Direccion.:' + String(beach[7]) + '</li>\
                          <li>Diferencia Mts.:' + String(beach[6]) + '</li>\
                        </ul>\
                        </div>\
                    </div>'
    createinfo(marker, info, map);

  }
}


function createinfo(marker, name, map) {
  google.maps.event.addListener(marker, "click", function () {
    if (infowindow) infowindow.close();
    infowindow = new google.maps.InfoWindow({content: name});
    infowindow.open(map, this);
  });
}

function setZoom(map, markers) {
    var boundbox = new google.maps.LatLngBounds();
    for ( var i = 0; i < markers.length; i++ )
    {
      boundbox.extend(new google.maps.LatLng(markers[i][1], markers[i][2]));
    }
    map.setCenter(boundbox.getCenter());
    map.fitBounds(boundbox);
    
}


