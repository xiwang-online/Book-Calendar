<template>
    <img class="backimg" src="../assets/background.jpg">
    <div class="cal">
        <div class="month">----- {{ data.time.month }}月 -----</div>
        <div class="day">{{ data.time.date }}</div>
        <hr width="66%">
        <div class="week">{{ data.time.week }}</div>
        <div class="yi">
            <span class="yit">宜</span>
            <span class="yic">{{ data.bookdata[0].yi }}</span>
        </div>

    </div>
    <div class="book" @click="details">
        <img class="bookpic" :src=data.bookdata[0].imagelink>
        <div class="bookname">《{{ data.bookdata[0].bookname }}》{{ data.bookdata[0].author }} {{ data.bookdata[0].bookdate }}
        </div>
        <div class="bookword">{{ data.bookdata[0].word }}</div>
        <div class="bookwn">--《{{ data.bookdata[0].bookname }}》</div>
    </div>

    <div class="foot">
        <div class="tit">读书日历</div>
        <div class="int">每天一本好书</div>
        <div class="about" @click="about">关于</div>
        <div class="submit" @click="submit">投稿</div>
        <div class="before" @click="before">往日推荐</div>
        <div class="support" @click="support">支持</div>
    </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import { useRouter } from "vue-router";
export default {
    //组件名
    name: 'home',
    setup() {
        const router = useRouter()
        let data = reactive({
            time: {
                year: "",
                month: "",
                date: "",
                hours: "",
                minutes: "",
                seconds: "",
                week: "",
                ymd: "", //年月日
            },
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

            //获取时间
            var dateObj = new Date();
            var year = dateObj.getFullYear(); //年
            var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
            var date = dateObj.getDate(); //日
            var day = dateObj.getDay();
            var weeks = [
                "星期日",
                "星期一",
                "星期二",
                "星期三",
                "星期四",
                "星期五",
                "星期六",
            ];
            var week = weeks[day]; //根据day值，获取星期数组中的星期数。
            var hours = dateObj.getHours(); //小时
            var minutes = dateObj.getMinutes(); //分钟
            var seconds = dateObj.getSeconds(); //秒
            /*
            if (month < 10) {
                month = "0" + month;
            }
            
            if (date < 10) {
                date = "0" + date;
            }
            */
            if (hours < 10) {
                hours = "0" + hours;
            }
            if (minutes < 10) {
                minutes = "0" + minutes;
            }
            if (seconds < 10) {
                seconds = "0" + seconds;
            }
            data.time.year = year;
            data.time.month = month;
            data.time.date = date;
            data.time.hours = hours;
            data.time.minutes = minutes;
            data.time.seconds = seconds;
            data.time.week = week;
            data.time.ymd = data.time.year + "." + data.time.month + "." + data.time.date

            axios.post('api/book/', {
                "action": 'list_book',
                //"time":"2023.2.18",
                "time": data.time.ymd,
            }).then(function (value) {
                //console.log(value);
                data.bookdata = value.data.retlist;
                console.log(data.bookdata)
            })
                .catch(function (reason) {
                    console.log(reason)
                })

        })





        function details() {
            //路由只传日期到详情页
            router.push({ path: '/bookdetails', query: { date: data.bookdata[0].date } })
        }

        function about() {

        }

        function submit() {
            router.push('/submit')

        }

        function before() {
            router.push('/booklist')

        }

        function support() {

        }





        //数据和函数都要返回
        return {
            data,
            details,
            about,
            submit,
            before,
            support
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

.cal {
    width: 260px;
    height: 350px;
    border-style: solid;
    border-color: white;
    position: absolute;
    top: 120px;
    left: 200px;

    display: flex;
    flex-direction: column;
    /*垂直排列*/
    align-items: center;
    justify-content: center;
    color: white;


}

.day {
    font-size: 166px;
    line-height: 166px;
}

.week {
    margin-top: 8px;
}

.yi {
    font-size: 36px;
    margin-top: 20px;
}

.yit {
    margin-right: 30px;

}

.book {
    position: absolute;
    bottom: 100px;
    right: 160px;
    width: 520px;
    display: flex;
    flex-direction: column;
    /*垂直排列*/
    align-items: flex-end;
    justify-content: center;
    color: white;
    cursor: pointer;

}

.bookpic {
    width: 150px;
    margin: 10px;
    opacity: 0.7;
}

.bookname {
    font-size: 20px;
}

.bookword {
    font-size: 36px;
    margin-top: 30px;
}

.bookwn {
    font-size: 36px;
}

.foot {
    position: absolute;
    left: 200px;
    bottom: 20px;
    display: flex;
    flex-direction: row;
    /*垂直排列*/
    align-items: center;
    justify-content: space-between;
    color: white;
    width: 500px;

}

.tit {
    font-size: 24px;
}

.submit {
    cursor: pointer;

}

.before {
    cursor: pointer;

}
</style>
