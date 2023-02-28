$(document).ready(function () {
	"use strict"; // start of use strict

	/*==============================
	Upload cover
	==============================*/
	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function(e) {
				$('#form_photo').attr('src', e.target.result);
			}
		
			reader.readAsDataURL(input.files[0]);
		}
	}
    
    function readURL2(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function(e) {
                $('#form_photo_back').attr('src', e.target.result);
			}
		
			reader.readAsDataURL(input.files[0]);
		}
	}

	$('#id_photo').on('change', function() {
		readURL(this);
	});
    
    $('#id_photo_back').on('change', function() {
		readURL2(this);
	});

	/*==============================
	Upload video
	==============================*/
	$('#id_manual').on('change', function() {
		var myFile = $('#id_manual').prop('files')[0];
        var canvas_elem = $( '<canvas class="snapshot-generator"></canvas>' ).appendTo(".field-manual label")[0];
        var $video = $( '<video muted class="snapshot-generator"></video>' ).appendTo(".field-manual label");
        var step_2_events_fired = 0;
        $video.one('loadedmetadata loadeddata suspend', function() {
          if (++step_2_events_fired == 3) {
            $video.one('seeked', function() {
              canvas_elem.height = this.videoHeight;
              canvas_elem.width = this.videoWidth;
              canvas_elem.getContext('2d').drawImage(this, 0, 0);
              var snapshot = canvas_elem.toDataURL();
              $('#form_video').attr('src', snapshot);
              // Delete the elements as they are no longer needed
              $video.remove();
              $(canvas_elem).remove();
            }).prop('currentTime', 6);
          }
        }).prop('src', URL.createObjectURL(myFile));
	});

	/*==============================
	Upload gallery
	==============================*/
	$('.form__gallery-upload').on('change', function() {
		var length = $(this).get(0).files.length;
		var galleryLabel  = $(this).attr('data-name');

		if( length > 1 ){
			$(galleryLabel).text(length + " files selected");
		} else {
			$(galleryLabel).text($(this)[0].files[0].name);
		}
	});

	

	/*==============================
	Bg
	==============================*/
	$('.section--bg').each( function() {
		if ($(this).attr("data-bg")){
			$(this).css({
				'background': 'url(' + $(this).data('bg') + ')',
				'background-position': 'center center',
				'background-repeat': 'no-repeat',
				'background-size': 'cover'
			});
		}
	});
    
    /*==============================
	Insert img inside label
	==============================*/
    $(".field-photo label").html("");
    $("#form_photo").appendTo(".field-photo label");
    $("#form_photo_back").appendTo(".field-photo_back label");
    $(".field-manual label").html("");
    $("#form_video").appendTo(".field-manual label");
    $("p.file-upload").remove();
    $("#flag_id_origen").remove();
    /*==============================
	Format form
	==============================*/
    $(".games").append('<div class="format"></div>');
    $(".field-name").appendTo(".format");
    $(".field-title_eng").appendTo(".format");  
    $(".games .field-title").appendTo(".format");
    $(".field-interpreter").appendTo(".format");    
    $(".games .field-year").appendTo(".format");
    $(".field-category").appendTo(".format");
    $(".field-display").appendTo(".format");
    $(".games .field-definition").appendTo(".format");
    $(".field-gender").appendTo(".format");
    $(".games .field-format").appendTo(".format");
    $(".field-place").appendTo(".format");
    $(".field-sub_gender").appendTo(".format");

    
    $(".games2").append('<div class="format2"></div>');
    $(".field-type").appendTo(".format");  
    $(".field-size").appendTo(".format2");
    $(".field-requirement").appendTo(".format2");
    $(".field-author").appendTo(".format2");
    $(".field-duration").appendTo(".format2");
    $(".field-saga").appendTo(".format2");
    $(".field-language").appendTo(".format2");
    $(".field-in_transmission").appendTo(".format2");
    $(".field-origen").appendTo(".format");
    $(".field-synopsis").appendTo(".format2");
    
    
    

});