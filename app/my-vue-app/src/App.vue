<template height="100%">
  <div id="app">
    <div id="overlay" v-show="showContent">
    <div id="content">
      <div class="drop_area" 
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
      <button class='upload-button' @click="sendFile">Upload</button>
    </div>
    </div>
    <router-view/> 
    <Navber v-show="show" @createModal="openModal"/>
  </div>
</template>


<script>
import Navber from './components/Navber'
//import axios from 'axios'

export default {
  name: 'App',
  components: {
  Navber
  },
  data() {
    return{
      showContent: false,
      isEnter: false,
      files:"",
      //files: [],
      show: false,
      caption:"",
      title:"",
    }
  },
  methods:{
    openModal: function(){
      this.showContent = true
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
    sendFile: function(this.files){
      if(this.files.length < 1) return
      this.files.forEach(file => {
        let formData = new FormData();
        formData.append("post",file)
      })
      fetch("http://0.0.0.0:8000/up/",{method: "POST",body: this.files})
    }
  },
  mounted() {
    let cookies = document.cookie; //全てのcookieを取り出して
    let cookiesArray = cookies.split(';'); // ;で分割し配列に
    console.log(cookiesArray)
    for(var c of cookiesArray){ //一つ一つ取り出して
        var cArray = c.split('='); //さらに=で分割して配列に
        if( cArray[0] == 'isLogin'){ // 取り出したいkeyと合致したら
            if( cArray[1] == 'true'){
              this.show = true;
            }
        }
    }
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
#content{
  z-index:2;
  width:30%;
  padding: 1em;
  background-color: #fff;
  border-radius: 30px;
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
  /* display: flex;
  justify-content: center;
  align-items: center; */
  width: auto;
  height: 8em;
  /* border: 5px solid gray; */
  border: 2px dashed #FFDD83;
  border-radius: 25px;
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
  border-radius: 100vh;
  margin-bottom: 1em;
  font-size: 16px;
}
</style>
