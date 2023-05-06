<template>
    <div class="main">
        <div class="title">读书日历 · 往期推荐</div>
        <booklistItem v-for="bookdata in data.bookdatas" :key="bookdata.id" :bookdata="bookdata" ></booklistItem>
        
    </div>
</template>
  
<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import booklistItem from '../components/booklistItem.vue'  //引入组件
export default {
    //组件名
    name: 'booklist',
    components: {
        booklistItem    //注册组件
    },
    setup() {
        let data = reactive({
            bookdatas:{}
        })



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post('api/book/', {
                "action": 'list_book',
                "time": 0,
            }).then(function (value) {
                //console.log(value);
                data.bookdatas = value.data.retlist;
                data.bookdatas = data.bookdatas.reverse() 
                //console.log(data.bookdatas)
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
    display: flex;
    flex-direction: column;
    /*垂直排列*/
    align-items: center;

}

.title {
    font-size: 64px;
    margin: 50px;
    color: white;

}
</style>
  