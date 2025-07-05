import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://htgs.ccgp.gov.cn/GS8/contractpublish/search",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "$HMF_CI": "9523cac8184798495287bcb2c640f467cd9809ea4845673beaf01829c633ad626ecbf47173e634a1958da3aff0ada061e344444e5eeaef260c3055c2e1c1b441e7",
    "JSESSIONIDGS8": "M9P8XeGYJUgLuTxC2gtdMIuEIjJfTlCtm4ZsDZqd-5bWAfQ8hmHA\\u0021-64666437",
    "cookieinsert": "20111186",
    "HMY_JC": "2ef3667763945c6f2c37e753ed3c7738b1aed9bc70ecdfb04589cb859b3cb64d3e,",
    "HBB_HC": "caeba5ad74dc8ca9fa0211317ec36e58a76dc26c32c7a534818301c539a82bf1b25744e64cd9b541f2fa55c9b6bd47ee3b"
}
url = "http://htgs.ccgp.gov.cn/GS8/genCodeImg"
params = {
    "t": "0.3029149997592778"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

print(response.text)
print(response)

# if(data.success){
# 				$("#codeImgDiv").empty();
# 				var $img = $('<img>');
# 				$img.attr("src",contextPath + "/upload/verifyCodes/" + data.msg + ".jpg");
# 				$img.height(30);
# 				$img.width(70);
# 				$img.css("vertical-align","middle");
# 				$img.click(function(){
# 					loadCodeImg();
# 				});
# 				$("#codeImgDiv").append($img);
# 				$("#codeResult").val(data.msg);
# 			}