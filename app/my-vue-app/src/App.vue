<template height="100%">
  <div id="app">
    <div id="overlay" v-show="showContent">
      <div class="content">
        <div v-if="uploadType == 'youtube'" class="drop_area center">
          <div>
            <input id="url" v-model="youtubeUrl" placeholder="URL"/><br>
            <input id="ttl" v-model="youtubeTitle" placeholder="タイトル"/><br>
            <textarea  id="caption" v-model="youtubeCaption"/>
          </div>
        </div>
        <div v-if="uploadType == 'own'"
        class="drop_area" 
        @dragenter="dragEnter"
        @dragLeave="dragLeave"
        @dragover.prevent
        @drop.prevent="dropFile" 
        :class="{enter:isEnter}">
          
          <div class="content-inner">
            
          <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#ffdd83" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 21H4a2 2 0 0 1-2-2V5c0-1.1.9-2 2-2h5l2 3h9a2 2 0 0 1 2 2v2M19 15v6M16 18h6"/></svg>
          <p>Drag & Drop Videos</p>
          </div>

        </div>
        
        <button class='cancel-button' @click="closeModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
        <button class='upload-button' v-if="uploadType == 'own'" @click="sendFile">ビデオを投稿</button>
        <button class='upload-button' v-if="uploadType == 'youtube'" @click="sendYoutube">Youtube動画を投稿</button>
        <div>
          <button @click="changePostType" class="post-change" v-if="uploadType == 'youtube'">自作動画の投稿</button>
          <button @click="changePostType" class="post-change" v-if="uploadType == 'own'">Youtubeの投稿</button>
        </div>
      </div>
      
    </div>



    <!-- コメントポップアップ -->
    <div id='overlay_comment' v-show='showCommentContent'>
      <Comment :info="info"
      @closeCommentModal="closeCommentModal"
      :commentContents="commentContents"/>
    </div>
    <!-- コメントポップアップ -->



    <router-view class="routerView" @openCommentModal="openCommentModal"/> 
    <Navber v-show="showNav" @createModal="openModal"/>
  </div>
</template>


<script>
import Navber from './components/Navber'
import Comment from './components/Comment'
import store from './store'
import {db} from './firebase'
import { collection, addDoc, getDocs, where, query} from 'firebase/firestore'

export default {
  name: 'App',
  components: {
  Navber,
  Comment,
  },
  data() {
    return{
      info:{},//コメントポップアップ用info
      commentContents:[],//コメントの中身
      showContent: false,
      showCommentContent: false, //コメントポップアップ用
      user_id:"",
      uploadType:"own",
      youtubeUrl:"",
      youtubeCaption:"",
      youtubeTitle:"",
      isEnter: false,
      files:"",
      //files: [],
      showNav: false,
      caption:"",
      title:"",
    }
  },
  methods:{
    openModal: function(){
      this.showContent = true
    },
    changePostType: function(){
      if(this.uploadType == "own"){
        this.uploadType = "youtube"
      }else{
        this.uploadType = "own"
      }
    },
    renderComment:async function(){
      let commentList = []
      const q = query(collection(db, "videogram/v1/comments"),where("postId", "==", this.info.id))
      await getDocs(q).then(result => {
        console.log(result.docs[0].data())
        result.docs.forEach((doc,key)=>{
          commentList[key] = doc.data().content
          })
        })
      commentList.forEach(result => this.commentContents.push(result))
      return commentList
    },

    openCommentModal: function(info){ //コメントポップアップ用
      this.info = info
      this.info.url = `${this.info.url.replace("https://www.youtube.com/embed/","https://img.youtube.com/vi/")}/maxresdefault.jpg`
      this.renderComment();
      this.showCommentContent = true
    }, 
    closeCommentModal: function(){
      this.showCommentContent = false
    },
    sendYoutube: async function(){
      console.log("youtube")
      if((this.youtubeUrl || this.youtubeTitle || this.youtubeCaption ) == ("")) {
        alert("全て記入してください")
        this.closeModal()
        return
      }
      await addDoc(collection(db, "videogram/v1/posts"), {
          url:this.youtubeUrl.replace("watch?v=","embed/"),
          title:this.youtubeTitle,
          caption:this.youtubeCaption,
          userId:`/users/${store.state.userId}`,
          likedNumber:0
      })
      this.closeModal()
    },
    closeModal: function(){
      this.showContent = false
    },
    dragEnter: function() {
      this.isEnter = true
    },
    dragLeave: function() {
      this.isEnter = false
    },
    dragOver: function() {
      console.log("dragg")
    },
    dropFile: function(event) {
      console.log(event.dataTransfer.types.includes("text/uri-list"))
      //this.files = [...event.dataTransfer.files]
      this.files = event.dataTransfer.getData('text');
      console.log(this.files)
      this.isEnter = false;
    },
    sendFile: function(){
      if(this.files.length < 1) return
      this.files.forEach(file => {
        let formData = new FormData();
        formData.append("post",file)
      })
      fetch("http://0.0.0.0:8000/up/",{method: "POST",body: this.files})
    }
  },
  mounted() {
    this.showNav = store.state.isLogin
    //ログインしていない時の処理を追記する
    if(store.state.isLogin == false && location.pathname == "/")this.$router.push("/login")
     if(store.state.isLogin == true && location.pathname == "/")this.$router.push("/home")
  },

}
</script>

<style>
#overlay{
  z-index:1;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(82, 81, 80, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;

}
.content{
  z-index:2;
  width:30%;
  padding: 1em;
  background-color: #fff;
  position:relative;
  box-shadow: 0px 2px 6px 0 rgba(82, 81, 80, 0.5);
}
.form{
  border: 1px #363124;
}
.drop_area {
  color: #444;
  font-weight: bold;
  font-size: 1.2em;
  width: auto;
  height: 8em;
  /* border: 5px solid gray; */
  border: 2px dashed #FFDD83;
  border-radius: 10px;
  /* margin:auto; */
  margin: 1em;
  position: relative;
}

.content-inner{
  position:absolute;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
}

.enter {
    border: 2px solid #FFDD83;
    border-radius: 25px;
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

.upload-button:hover {
  background-color: #ffedbd;
}

.upload-button{
  color: #fff;
  background-color: #FFDD83;
  padding: 10px 30px;
  border: none;
  font-weight: bold;
  border-radius: 100vh;
  font-size: 16px;
  margin-top: 0.5em;
}

#overlay_comment{
  z-index:1;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(82, 81, 80, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.center{
  display: flex;
  justify-content: center;
  align-items: center;
}

.post-change{
  background-color: transparent;
  border: none;
  text-decoration: underline;
  font-size: 0.8em;
  margin: 0.5em 0 1em 0;
}

.post-change:hover{
  color: #777;
}

</style>
