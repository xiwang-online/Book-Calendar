<template>
    <img class="backimg" src="../assets/submit.jpg">
    <div class="main">
        <div class="content">
            <div class="mar">
                <div class="title">读书日历 · 投稿书籍</div>
                <div class="beginword">把你喜欢的书提交给读书日历吧，通过我们分享给更多喜欢读书的小伙伴们~ 谢谢你的分享！</div>
                <div class="booknamet">书名：</div>
                <el-input v-model="data.adddata.bookname" size="large" placeholder="书名" />
                <div class="authort">作者：</div>
                <el-input v-model="data.adddata.author" placeholder="作者" />
                <div class="reasont">推荐理由：</div>
                <el-input v-model="data.adddata.introduction" :rows="5" type="textarea" placeholder="推荐理由" />
                <div class="informationt">联系方式：</div>
                <el-input v-model="data.adddata.information" placeholder="联系方式" />
                <el-button @click="submit">提交</el-button>
            </div>
        </div>
    </div>esd
</template>
  
<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
export default {
    //组件名
    name: 'submit',
    setup() {
        let data = reactive({
            adddata: {
                date: "",
                bookname: "",
                author: "",
                introduction: "",
                information: "",
                remark: "",
                spare1: "",
                spare2: "",

            }



        })



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {

        })

        function submit() {

            //获取时间
            var dateObj = new Date();
            var year = dateObj.getFullYear(); //年
            var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
            var date = dateObj.getDate(); //日
            var hours = dateObj.getHours(); //小时
            var minutes = dateObj.getMinutes(); //分钟
            data.adddata.date = year +"."+ month +"."+ date +"."+ hours +"."+ minutes

            if (data.adddata.bookname === "") {
                alert("书名不能为空！")
            } else {
                axios.post("api/submit/", {
                    "action": "add_submit",
                    "data": data.adddata
                }).then(function (response) {
                    if (response.data.ret == 0) {
                        data.adddata.date = ""
                        data.adddata.bookname = ""
                        data.adddata.author = ""
                        data.adddata.introduction = ""
                        data.adddata.information = ""
                        data.adddata.remark = ""
                        data.adddata.spare1 = ""
                        data.adddata.spare2 = ""
                        alert("提交成功");
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert("未知错误");
                });
            }
        }




        //数据和函数都要返回
        return {
            data,
            submit
        }
    },



}
</script>
<style scoped>
.backimg {
    position: fixed;
    width: 100%;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
}

.main {
    min-height: 100vh;
    display: flex;
    display: flex;
    justify-content: center;
    align-items: center;

}

.content {
    width: 50%;
    height: 70vh;
    background-color: bisque;
}

.mar {
    padding: 10px 100px;
}

.title {
    font-size: 35px;
    margin: 25px;
    text-align: center;

}
</style>
  