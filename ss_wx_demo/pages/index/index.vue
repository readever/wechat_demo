<template>
	<view class="content wrapper">
		
       <view class="uni-list mylist">

			<view class="tag">
				SimpleStart 让您可以轻松地利用 Python 创建交互式应用程序和数据可视化。
			</view>
			
			<view>
				<button type="default" @click="testme">进入</button>
			</view>
	
        </view>		

	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {
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
				testme:function(){
					uni.navigateTo({
						url: "/pages/webview/webview"
					})
				},
				testme2:function(){
					uni.navigateTo({
						url: "/pages/webview/webview?test=1"
					})
				}

		}
	}
</script>

<style>
	.mylist{
		margin:5%;
		background:white;
		margin-top:20%;
		padding:10px;
		border-radius: 5px;
	}

	.mylist:before {
		height:0;
	}

	.mylist:after {
		height:0;
	}

	.mylist .tag{
		color:#73767a;
		margin-top:3px;
	}
	.tag{
		margin-top:30px;
		margin-bottom:30px;
		padding-bottom:10px;
		border-bottom:1px solid #73767a;
		color:#337ecc;
		font-weight: bold;
		line-height: 30px;
	}
	
.wrapper {
    background: #5898d4;
    overflow: hidden;
	height:calc(100vh)
}
button{
	background-color:#5898d4 !important;
	color:white !important;
	width:50%;
	z-index:999;
}
</style>
