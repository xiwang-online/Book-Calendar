<template>
    <div class="main">
    <div class="details">
        <div class="header">读书日历</div>
        <div class="book">
            <div class="left">
                <div class="name">{{data.bookdata[0].bookname}}</div>
                <div class="aut">作者：{{ data.bookdata[0].author }}</div>
                <div class="word">"{{ data.bookdata[0].word }}"</div>
                <div class="int">{{ data.bookdata[0].introduction }}</div>
            </div>
            <div class="right">
                <img class="bookpic"
                    :src=data.bookdata[0].imagelink>
            </div>
        </div>
    </div>
    <div class="booklink">作者简介: {{ data.bookdata[0].authorintroduction }}</div>
</div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import { useRoute } from "vue-router";
export default {
    //组件名
    name: 'bookdetails',
    setup() {
        const route = useRoute()
        let data = reactive({
            bookdata: [{
                "date": "",
                "bookname": "",
                "author": "",
                "bookdate": "",
                "word": "",
                "introduction": "",
                "authorintroduction": "",
                "downloadlink": "",
                "imagelink": "",
                "yi": "",
                "label": "",
                "remark": "",
                "spare1": "",
                "spare2": ""
            }]
            
        })



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            //接收home页面的日期，然后从后端获取详细信息
            axios.post('api/book/', {
                "action": 'list_book',
                "time": route.query.date,
            }).then(function (value) {
                //console.log(value);
                data.bookdata = value.data.retlist;
                console.log(data.bookdata)
            })
                .catch(function (reason) {
                    console.log(reason)
                })
        })


        //数据和函数都要返回
        return {
            data,
        }
    },



}
</script>

<style scoped>
.main {
    background-color: #1b161a;
    min-height: 100vh;
}
.details {
    background-color: #0f0d10;
    color: white;
    padding: 20px 0px 80px 0px;
}

.header {
    font-size: 24px;
    margin: 20px 0px 50px 160px;
}

.book {
    border-style: solid;
    border-color: white;
    margin: 50px 160px;
    display: flex;
    padding: 50px;
}

.left {
    margin-right: 150px;
}

.name {
    font-size: 36px;
    margin-bottom: 5px;

}

.aut {
    font-size: 18px;
}

.word {
    font-size: 24px;
    margin: 40px 0px 20px 0px;
}

.int {
    font-size: 15px;
    text-indent: 2em;
}


.bookpic {
    width: 220px;
    height: 310px;
}


.booklink {
    color: #999999;
    font-size: 15px;
    margin: 50px 180px 0px 180px;
    padding-bottom: 50px;

}


</style>
