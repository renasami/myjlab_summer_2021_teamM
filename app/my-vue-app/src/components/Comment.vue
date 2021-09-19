<template>
    <div class="comment">
        <button @click="closeCommentModal">button</button><br/>
        <input type="textbox" v-model="content"/><br/>
        <button @click="sendComment">send</button><br/>
        <button @click="getComment">get</button>
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
.comment{
    width:500px;
    height:500px;
}
</style>
