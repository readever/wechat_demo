<template>
	<view>
		<web-view :webview-styles="webviewStyles" :src="webSrc" @back="onback"></web-view>	
	</view>
</template>

<script>
	//https://m.php.cn/faq/546195.html
	export default {
		data() {
			return {
				title: 'Hello1',
				//webSrc:"https://m.baidu.com"
				//webSrc:"http://localhost:3000/pages/menulist",
				webSrc:"http://192.168.0.8:8000/pages/menulist",
				//webSrc:"http://192.168.0.8:8010/test.html#/",
				//webSrc:"https://docs.h5book.cn/pages/menulist",
				///测试别的移动框架的速度
				//webSrc : "https://m.h5book.cn",
				///webSrc : "https://hellouniapp.dcloud.net.cn/",
			}
		},
		onLoad(options) {
			console.log(options);

			/*
			wx.enableAlertBeforeUnload({
				message:"返回上页时弹出对话框",
				success: function (res){
					console.log("方法注册成功:", res);
				}
			});
			*/
		},
		
		onUnload() {
			console.log("onunload")
		},

		methods: {
			    // 自定义此页面的转发给好友(已经有全局的分享方法，此处会覆盖全局)
				onShareAppMessage(res) {
				    return {
				      title: 'SimpleStart Python 前端开发和数据处理框架',
				      path: '/pages/index/index',
					  imageUrl: '/static/screen1.jpg'
				    }
				  },
				  // 自定义页面的分享到朋友圈
				onShareTimeline(res) {
					return {
						title: 'SimpleStart Python 前端开发和数据处理框架',
						path: '/pages/index/index',
						imageUrl: '/static/screen1.jpg'
					}
				},	
				onPageLoad(e) {
				      console.log('Loaded page: ' + e.url)
				},
				onback(e) {
				  // 获取即将加载页面的url
				  console.log("xxx", e.url) 
				  
				  // 在此处可进行页面拦截、提示等自定义逻辑
				  //if(不符合条件) {
					// 阻止加载新页面
					e.preventDefault()  
				  //}
				}
		}
	}
</script>

<style>

</style>
