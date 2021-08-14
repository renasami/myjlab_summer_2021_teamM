<template height="100%">
  <div id="app">
    <div id="overlay" v-show="showContent"  >
    <div id="content">
      <h1>post</h1>
      <div class="drop_area" 
      @dragenter="dragEnter"
      @dragLeave="dragLeave"
      @dragover.prevent
      @drop.prevent="dropFile" 
      :class="{enter:isEnter}">
          ファイルアップロード
      </div>
      <p><button @click="closeModal">close</button></p>
      <button @click="sendFile">送信</button>
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
      files:[],
      show: true,
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
      console.log(event.dataTransfer.files)
      this.files = [...event.dataTransfer.files]
      this.isEnter = false;
    },
    sendFile: function(){
      if(this.files.length < 1) return
      this.files.forEach(file => {
        let formData = new FormData();
        formData.append("post",file)
        fetch("http://0.0.0.0:8000/posts/",{method: "POST",body: formData})
      })
    }
  },
  beforeCreate() {
    
  },
//   watch: {
//   '$route': function (to) {
//     console.log(to.name)
//     if(to.name != 'login' || to.name != 'register') {
//       this.show = true;
//       return 
//     }
//     if(to.name == 'login' || to.name == 'register'){
//       this.show = false;
//     }
//   }
// }
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
  background-color:rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;

}
#content{
  z-index:2;
  width:50%;
  padding: 1em;
  background:#fff;
}
.drop_area {
  color: gray;
  font-weight: bold;
  font-size: 1.2em;
  display: flex;
  justify-content: center;
  align-items: center;
  width: auto;
  height: 8em;
  border: 5px solid gray;
  border-radius: 15px;
  margin:auto;
}
.enter {
    border: 10px dotted powderblue;
}
</style>
