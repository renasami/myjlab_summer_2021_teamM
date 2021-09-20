<template>
<div class="card">
<component-children v-bind:variable="list" />
    <div v-for="(items, index) in groupedArray" :key="index">
        <li class='cards' v-for="(item,itemInd) in items" :key="itemInd+index">
          <div class='cards_inner'>
          <Cardmin 
          :id="item.id"
          :uid="item.uid"
          :title="item.title"
          :caption="item.caption"
          :url="item.url"
          :samb="item.samb"
          :likedNumber="item.likedNumber"
          :isLike="item.isLike"
          :comment="item.comment"
          :index="itemInd+index"
          :like="like"
          :openCommentModal="openCommentModal"/>    
          </div>
        </li>
    </div>
    
</div>
</template>

<script>
import Cardmin from './Cardmin.vue'
import store from '../store'
import { db } from '../firebase'
import { doc, setDoc, query,collection,getDocs,where} from 'firebase/firestore'


export default {
    name: 'Card',
    components: {
      Cardmin
    },
   data: function () {
     return {
        list: this.posts,
        likedList:[],
        userData:{},
        userPrimarykey:""
     }
   },
   props:["posts","types"],
   methods:{
      like:async function(index){
        //userのlikeに対しての処理
        this.list[index].isLike = !this.list[index].isLike
        const q = query(collection(db,"videogram/v1/users"),where("uid","==",store.state.userId))
        await getDocs(q).then(ret =>ret.docs[0]).then(res => {
          this.userPrimarykey = res.id
          this.userData = res.data()
          })
        if(this.list[index].isLike){
          this.likedList.push(this.list[index].id)
        }else{
          this.likedList = this.likedList.filter(item => item != this.list[index].id)
        }
        await setDoc(doc(db,"videogram/v1/users",this.userPrimarykey),{
          email:this.userData.email,
          image:this.userData.image,
          uid:this.userData.uid,
          like: this.likedList
        })
        store.commit("setState","likedList",this.likedList)
      },
      openCommentModal:function(index){
        this.$emit("openCommentModal",this.list[index])
      }  
   },
  computed: {
    groupedArray() {
      const base = this.list?.length
      const split_cnt = 3       // 何個ずつに分割するか
      const grouped_list = []
      for (let i=0; i<Math.ceil(base/split_cnt); i++) {
        let multiple_cnt = i * split_cnt  // 3の倍数
        // (i * 3)番目から(i * 3 + 3)番目まで取得
        let result = this.list.slice(multiple_cnt, multiple_cnt + split_cnt) 
        grouped_list.push(result)
      }
      return grouped_list
    },
  },
    watch:{
      list:function(){
          this.list.forEach((item,index) => {
            this.likedList.forEach((liked) => {
            if(item.id == liked) this.list[index].isLike = true
          })
        })
        if(this.types == "like"){
          console.log("fas")
        }
      }
      
    },
  mounted: async function(){
        const q = query(collection(db,"videogram/v1/users"),where("uid","==",store.state.userId))
        await getDocs(q).then(ret =>ret.docs[0]).then(res => {this.likedList = res.data().like})
    },
  }




</script>

<style scoped>
.card {
  width:100%;
  position: absolute;
  right: 0;
  margin-top: 50px;
}

.cards {
  width:320px;
  margin: 20px 20px;
  display: inline-block;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
  background-color: white;
  cursor: pointer;
  transition-duration: 0.4s;
}

.cards:hover{
        transform: scale(1.1);
        transition-duration: 0.4s;
      }

.cards_inner {
  margin: 0 auto;
}

.upper_video {
  width:100%;
  height:75%;
  background-color:#F7F7F7;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
}

.lower_text {
  width:100%;
  height:25%;
  margin-top:10px;
  display: flex;
  justify-content: space-between;
}

.title, .icon {
  display: inline-block;
}

.title {
  font-size: 1.2em;
}

.after_button {
  fill: #E36C9E;
  stroke: #E36C9E;
}

.like_button {
  float: left;
}

@media (min-width: 960px) {
/*********************************************************
  Stylesheet: 960px以上のタブレットやモニタで適用
*********************************************************/
.card{
  width:80%;
}
}
</style>