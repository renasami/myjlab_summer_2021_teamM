<template>
    <div class="comment">

        <!-- サムネイル -->
        <div class="left">
            <img class="video-thumbnail" src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" alt="">
        </div>
        <!-- サムネイル -->


        <div class="right">
            <!-- キャンセルボタン -->
            <button @click="closeCommentModal" class="cancel-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
            <!-- キャンセルボタン -->

            <!-- 投稿者情報 -->
            <div class="comment-user">
                <p>動画投稿者名</p>
            </div>
            <!-- 投稿者情報 -->
            
            <!-- コメントリスト -->
            <div class="comment-list"> 
                <ul class="list-inner">
                    <li>おもしろい</li>
                    <li>爆笑</li>
                    <li>最高</li>
                </ul>
            </div>
            <!-- コメントリスト -->

            <!-- いいね＆コメント -->
            <div class="comment-icon">
                <button><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>
                <button><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></button>
            </div>
            <!-- いいね＆コメント -->


            <!-- コメント投稿 -->
            <div class="comment-post">
                <input type="textbox" class="post-text" v-model="content" placeholder="コメントを追加..."/>
                <button class="post-button" @click="sendComment">投稿</button>
                <!-- <button @click="getComment">get</button> -->
            </div>
            <!-- コメント投稿 -->


        </div>

    </div>    
</template>

<script>
import store from '../store'
import {db} from '../firebase'
import { addDoc, collection, getDocs, where, query} from 'firebase/firestore'

export default {
    name:'Comment',
    data(){
        return{
            content:'',
            comments:[]
        }
    },
    props: ["info"],
    methods:{
        closeCommentModal:function(){
            this.$emit('closeCommentModal')
        },
        sendComment: function(){
            console.log(db)
            addDoc(collection(db, 'videogram/v1/comments'), 
            {content: this.content,
             postId:this.info.id,
             uid: store.state.userId,
            })
        },
        getComment:async function(){
            const q = query(collection(db, "videogram/v1/comments"),where("postId", "==", this.info.id))
            const comments = await getDocs(q);
            // const list = comments.map((doc) => {
            //     // doc.data() is never undefined for query doc snapshots
            //     console.log({
            //     uid: doc.data().uid,
            //     content: doc.data().content
            //     });
            // });
            comments.forEach(doc => console.log(doc.data()));
            //console.log(comments)
        }
    },
}
</script>

<style scoped>

button {
    border: none;
    background-color: transparent;
}

.comment{
    width:50%;
    height:60%;
    background-color: white;
    display: flex;
}

.left{
    width: 60%;
    height:100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #eaeaea;
}

.video-thumbnail{
    width:100%;
}

.right {
    position:relative;
    width:40%;
    height:100%;
    text-align: left;
}

.cancel-button {
    background-color: transparent;
    border: none;
    position: absolute;
    top: 0.2em;
    right: 0.4em;
    font-size: 35px;
    color:rgba(0, 0, 0, 0.4);
    font-weight: 100;
}

.comment-user{
    height: 15%;
    border-bottom: 1px solid #eaeaea;
    padding: 0 10px 0 10px;
    display: flex;
    align-items: center;
    font-weight:bold;
}

.comment-list{
    height: 65%;
    overflow: scroll;
    border-bottom: 1px solid #eaeaea;
}

.list-inner{
    list-style: none;
    padding: 10px;
}

.comment-icon{
    height:10%;
    padding: 0 10px 0 10px;
    border-bottom: 1px solid #eaeaea;
    display: flex;
    align-items: center;
}

.comment-post{
    height:10%;
    padding: 0 10px 0 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.post-button{
    font-weight: bold;
    color:#CF2E92;
}

.post-text{
    border: none;
    width:80%;
}

.post-text:focus{
    outline: none;
}
</style>