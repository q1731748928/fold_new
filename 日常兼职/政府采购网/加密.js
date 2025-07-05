function loadCodeImg(){
		$.getJSON(contextPath + "/genCodeImg?t=" + Math.random(),{},function(data){
			if(data.success){
				$("#codeImgDiv").empty();
				var $img = $('<img>');
				$img.attr("src",contextPath + "/upload/verifyCodes/" + data.msg + ".jpg");
				$img.height(30);
				$img.width(70);
				$img.css("vertical-align","middle");
				$img.click(function(){
					loadCodeImg();
				});
				$("#codeImgDiv").append($img);
				$("#codeResult").val(data.msg);
			}else{
				$("#codeResult").val("");
				alert("验证码加载失败，请联系管理员。")
			}
		});
	}

console.log(loadCodeImg());