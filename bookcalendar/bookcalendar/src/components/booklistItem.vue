<template>
    <div class="content">
        <div class="left">
            <div class="date">{{data.bookdata.date}}</div>
            <div class="ym">{{data.bookdata.ym}}</div>
            <div class="week">{{data.bookdata.week}}</div>
        </div>
        <div class="right" @click="detail(data.bookdata.ymd)">
            <img class="bookpic" :src=data.bookdata.imagelink>
            <div class="bookinf">
                <div class="name">{{ data.bookdata.bookname }}</div>
                <div class="aut">{{data.bookdata.author}} {{ data.bookdata.bookdate }}</div>
                <div class="word">{{ data.bookdata.word }}</div>
            </div>

        </div>

    </div>
</template>
  
<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import { useRouter } from "vue-router";
export default {
    //组件名
    name: 'booklistItem',
    props: ['bookdata'],//接收参数
    setup(props) {
        const router = useRouter()
        let data = reactive({
            bookdata: {
                "id":"",
                "ymd":"",//年月日
                "date": "",//日期
                "ym": "",//年月
                "week": "",//星期
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
            }

        })

        onMounted(() => {
            data.bookdata.id = props.bookdata.id
            data.bookdata.ymd = props.bookdata.date
            data.bookdata.date = props.bookdata.date.split(".")[2]
            data.bookdata.ym = props.bookdata.date.split(".")[0] + "年" + props.bookdata.date.split(".")[1] + "月"
            data.bookdata.week = getweekday(props.bookdata.date)
            data.bookdata.bookname = props.bookdata.bookname
            data.bookdata.author = props.bookdata.author
            data.bookdata.bookdate = props.bookdata.bookdate
            data.bookdata.word = props.bookdata.word
            data.bookdata.introduction = props.bookdata.introduction
            data.bookdata.authorintroduction = props.bookdata.authorintroduction
            data.bookdata.downloadlink = props.bookdata.downloadlink
            data.bookdata.imagelink = props.bookdata.imagelink
            data.bookdata.yi = props.bookdata.yi
            data.bookdata.label = props.bookdata.label
            data.bookdata.remark = props.bookdata.remark
            data.bookdata.spare1 = props.bookdata.spare1
            data.bookdata.spare2 = props.bookdata.spare2
        })

        //通过日期获取周几
        function getweekday(date) {
            var weekArray = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六");
            var week = weekArray[new Date(date).getDay()];//注意此处必须是先new一个Date
            return week;
        }


        function detail(ymd) {
            router.push({ path: '/bookdetails', query: { date: ymd } })

        }





        //数据和函数都要返回
        return {
            data,
            detail
        }
    },




}
</script>

<style scoped>
.content {
    width: 60vw;
    display: flex;
    flex-direction: row;
    /*垂直排列*/
    justify-content: space-between;
    align-items: center;
    color: white;
    /*边框*/
    border-bottom-style: solid;
    border-color: white;

}

.left {
    display: flex;
    flex-direction: column;
    /*垂直排列*/
    justify-content: center;
    align-items: center;
    margin: 30px 0px 50px 50px;
}

.date {
    font-size: 84px;
    line-height: 84px;
}

.right {
    display: flex;
    flex-direction: row;
    /*垂直排列*/
    justify-content: flex-start;
    align-items: flex-start;
    width: 60%;
    cursor: pointer;
}

.bookpic {
    width: 100px;
    height: 144px;
    margin: 20px 20px;
    opacity: 0.7;
}

.bookinf {
    min-height: 144px;
    margin-top: 20px;
}

.name {
    font-size: 24px;

}

.word {
    font-size: 18px;
    margin-top: 30px;
}
</style>
  