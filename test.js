/**
 * Created by windpro on 14-9-3.
 */
$.ajax({
    async: false,
    url: "http://cache.codedig.com/blogcache/test.json",
    type: "GET",
    dataType: 'jsonp',
    jsonpCallback: "L2FwaS90ZXN0YXBp",// /api/testapi base64加密字符串
    timeout: 5000,
    beforeSend: function (xhr) {   //beforeSend定义全局变量
        xhr.setRequestHeader("Referer", "http://www.baidu.com");  //Authorization 需要授权,即身体验证
    },
    success: function (json) {//客户端jquery预先定义好的callback函数,成功获取跨域服务器上的json数据后,会动态执行这个callback函数
        console.log(json.name);
    },
    complete: function (XMLHttpRequest, textStatus) {
        console.log(textStatus);
    },
    error: function (xhr) {
        //jsonp 方式此方法不被触发.原因可能是dataType如果指定为jsonp的话,就已经不是ajax事件了
        //请求出错处理
        alert("请求出错(请检查相关度网络状况.)");
    }
});