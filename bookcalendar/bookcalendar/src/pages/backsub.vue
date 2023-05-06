date = 
    bookname = 
    author = 
    introduction = 
    information = 
    remark = 
    spare1 = 
    spare2 = 
<template>
    <div class="main">
        <el-table :data="data.submits" height="85vh" style="width: 100%">
            <el-table-column type="index" width="50" />
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="date" label="提交日期" width="150" :show-overflow-tooltip='true'/>
            <el-table-column prop="bookname" label="书名" width="200" :show-overflow-tooltip='true'/>
            <el-table-column prop="author" label="作者" width="150" />
            <el-table-column prop="introduction" label="推荐理由" width="500" :show-overflow-tooltip='true' />
            <el-table-column prop="information" label="推荐人联系方式" width="300" :show-overflow-tooltip='true' />
            <el-table-column prop="remark" label="备注" width="100"/>
            <el-table-column prop="spare1" label="备用1" width="100" />
            <el-table-column prop="spare2" label="备用2" width="100" />

            <el-table-column fixed="right" label="Operations" width="120">
                <template #default="scope">
                    <el-popconfirm title="确定要删除吗?" @confirm="deletebook(scope.row.id)">
                        <template #reference>
                            <el-button link type="primary">删除</el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
export default {
    //组件名
    name: 'backsub',
    setup() {
        let data = reactive({
            submits: [],
            
        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/submit/", {
                "action": "list_submit",
            })
                .then(function (value) {
                    if (value.data.ret == 0) {
                        data.submits = value.data.retlist;
                    } else if (value.data.ret == 302) {
                        alert("未登录");
                        router.push("signin");
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert("未知错误");
                });
        })

       

        function deletebook(id) {
            axios.post("api/submit/", {
                "action": "del_submit",
                "id": id,
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.submits = data.submits.filter((submit) => { return submit.id != id })   //从数组中去掉被删掉的数据
                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });
        }




        //数据和函数都要返回
        return {
            data,
            deletebook,
        }
    },
}
</script>
<style scoped>
.main {
    width: 100%;
    height: 100%;
}



.but {
    margin: 20px 5px;
}

span {
    font-size: 20px;
    font-weight: 900;
}
</style>
