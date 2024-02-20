<script>
	export default {
		onLaunch: function() {
			console.log('App Launch');

			wx.preloadWebview({
			  url: 'pages/webview/webview' ,// webview页面路径 
			    complete(res) {
			      // 这里是preload完成后的回调函数
			      
			      if (res.errMsg === 'preloadWebview:ok') {
			        // preload成功
					console.log(res);
			      } else {
			        // preload失败
					console.log(res);
			      }
			    }
			})
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
		
	}
</script>

<style>
	/*每个页面公共css */
</style>
