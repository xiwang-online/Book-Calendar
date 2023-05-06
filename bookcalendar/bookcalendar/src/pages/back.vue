<template>
    <div class="main">
        <el-table :data="data.books" height="85vh" style="width: 100%">
            <el-table-column type="index" width="50" />
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="date" label="日期" width="90" />
            <el-table-column prop="bookname" label="书名" width="150" />
            <el-table-column prop="author" label="作者" width="150" />
            <el-table-column prop="bookdate" label="出版日期" width="100" />
            <el-table-column prop="word" label="摘录" width="190" :show-overflow-tooltip='true' />
            <el-table-column prop="introduction" label="简介" width="190" :show-overflow-tooltip='true' />
            <el-table-column prop="authorintroduction" label="作者简介" width="190" :show-overflow-tooltip='true' />
            <el-table-column prop="downloadlink" label="下载链接" width="80" :show-overflow-tooltip='true' />
            <el-table-column prop="imagelink" label="封面链接" width="80" :show-overflow-tooltip='true' />
            <el-table-column prop="yi" label="宜" width="100" />
            <el-table-column prop="label" label="标签" width="100" />
            <el-table-column prop="remark" label="备注" width="50" :show-overflow-tooltip='true' />
            <el-table-column prop="spare1" label="时间戳" width="120" />
            <el-table-column prop="spare2" label="备用" width="100" :show-overflow-tooltip='true' />

            <el-table-column fixed="right" label="Operations" width="120">
                <template #default="scope">
                    <el-button link type="primary" @click="modify(scope.row)">修改</el-button>
                    <el-popconfirm title="确定要删除吗?" @confirm="deletebook(scope.row.id)">
                        <template #reference>
                            <el-button link type="primary">删除</el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
        <el-button class="but" type="primary" @click="add">添加</el-button>

        <el-dialog v-model="data.modifydialog" title="修改">
            <span>ID:{{ data.modifydata.id }}</span><br>
            <span>日期:</span>
            <el-input v-model="data.modifydata.date" />
            <span>书名:</span>
            <el-input v-model="data.modifydata.bookname" />
            <span>作者:</span>
            <el-input v-model="data.modifydata.author" />
            <span>出版日期:</span>
            <el-input v-model="data.modifydata.bookdate" />
            <span>摘录:</span>
            <el-input v-model="data.modifydata.word" />
            <span>简介:</span>
            <el-input v-model="data.modifydata.introduction" />
            <span>作者简介:</span>
            <el-input v-model="data.modifydata.authorintroduction" />
            <span>下载链接:</span>
            <el-input v-model="data.modifydata.downloadlink" />
            <span>封面链接:</span>
            <el-input v-model="data.modifydata.imagelink" />
            <span>宜:</span>
            <el-input v-model="data.modifydata.yi" />
            <span>标签:</span>
            <el-input v-model="data.modifydata.label" />
            <span>备注:</span>
            <el-input v-model="data.modifydata.remark" />
            <span>时间戳:</span>
            <el-input v-model="data.modifydata.spare1" />
            <span>备用:</span>
            <el-input v-model="data.modifydata.spare2" />
            <el-button class="but" type="primary" @click="modifysubmit">提交</el-button>
        </el-dialog>


        <el-dialog v-model="data.adddialog" title="添加">
            <span>日期:</span>
            <el-input v-model="data.adddata.date" />
            <span>书名:</span>
            <el-input v-model="data.adddata.bookname" />
            <span>作者:</span>
            <el-input v-model="data.adddata.author" />
            <span>出版日期:</span>
            <el-input v-model="data.adddata.bookdate" />
            <span>摘录:</span>
            <el-input v-model="data.adddata.word" />
            <span>简介:</span>
            <el-input v-model="data.adddata.introduction" />
            <span>作者简介:</span>
            <el-input v-model="data.adddata.authorintroduction" />
            <span>下载链接:</span>
            <el-input v-model="data.adddata.downloadlink" />
            <span>封面链接:</span>
            <el-input v-model="data.adddata.imagelink" />
            <span>宜:</span>
            <el-input v-model="data.adddata.yi" />
            <span>标签:</span>
            <el-input v-model="data.adddata.label" />
            <span>备注:</span>
            <el-input v-model="data.adddata.remark" />
            <span>时间戳:</span>
            <el-input v-model="data.adddata.spare1" />
            <span>备用:</span>
            <el-input v-model="data.adddata.spare2" />

            <el-button class="but" type="primary" @click="addsubmit">提交</el-button>
        </el-dialog>

    </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
export default {
    //组件名
    name: 'back',
    setup() {
        let data = reactive({
            books: [],
            modifydialog: false,   //修改框是否显示
            modifydata: {},  //要修改的数据
            adddialog: false,
            adddata: {
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

            }
        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/book/", {
                "action": "list_book",
                "time": -1
            })
                .then(function (value) {
                    if (value.data.ret == 0) {
                        data.books = value.data.retlist;
                    } else if (value.data.ret == 302) {
                        alert("未登录");
                        router.push("signin");
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert("未知错误");
                });
        })

        function add() {
            data.adddialog = true
        }


        function addsubmit() {
            axios.post("api/book/", {
                "action": "add_book",
                "data": data.adddata
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.adddialog = false
                    const bookObj = {
                        "id": response.data.id,
                        "date": data.adddata.date,
                        "bookname": data.adddata.bookname,
                        "author": data.adddata.author,
                        "bookdate": data.adddata.bookdate,
                        "word": data.adddata.word,
                        "introduction": data.adddata.introduction,
                        "authorintroduction": data.adddata.authorintroduction,
                        "downloadlink": data.adddata.downloadlink,
                        "imagelink": data.adddata.imagelink,
                        "yi": data.adddata.yi,
                        "label": data.adddata.label,
                        "remark": data.adddata.remark,
                        "spare1": data.adddata.spare1,
                        "spare2": data.adddata.spare2,
                    };
                    data.books.push(bookObj)
                    data.adddata.date = ""
                    data.adddata.bookname = ""
                    data.adddata.author = ""
                    data.adddata.bookdate = ""
                    data.adddata.word = ""
                    data.adddata.introduction = ""
                    data.adddata.authorintroduction = ""
                    data.adddata.downloadlink = ""
                    data.adddata.imagelink = ""
                    data.adddata.yi = ""
                    data.adddata.label = ""
                    data.adddata.remark = ""
                    data.adddata.spare1 = ""
                    data.adddata.spa2 = ""

                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });
        }

        function deletebook(id) {
            axios.post("api/book/", {
                "action": "del_book",
                "id": id,
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
                    data.books = data.books.filter((book) => { return book.id != id })   //从数组中去掉被删掉的数据
                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });
        }




        function modify(da) {
            data.modifydata = da
            data.modifydialog = true
        }
        function modifysubmit() {
            axios.post("api/book/", {
                "action": "modify_book",
                "id": data.modifydata.id,
                "newdata": {
                    "date": data.modifydata.date,
                    "bookname": data.modifydata.bookname,
                    "author": data.modifydata.author,
                    "bookdate": data.modifydata.bookdate,
                    "word": data.modifydata.word,
                    "introduction": data.modifydata.introduction,
                    "authorintroduction": data.modifydata.authorintroduction,
                    "downloadlink": data.modifydata.downloadlink,
                    "imagelink": data.modifydata.imagelink,
                    "yi": data.modifydata.yi,
                    "label": data.modifydata.label,
                    "remark": data.modifydata.remark,
                    "spare1": data.modifydata.spare1,
                    "spare2": data.modifydata.spare2,
                },
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
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
            modify,
            modifysubmit,
            add,
            addsubmit
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
