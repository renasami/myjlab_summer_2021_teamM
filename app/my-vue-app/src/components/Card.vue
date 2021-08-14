<template>
<div class="card">
    <div v-for="(items, index) in groupedArray" :key="index">
        <li class='cards' v-for="(item, index) in items" :key="index">
        <div class='cards_inner'>
        <div class='upper_video'></div>
        <div class='lower_text'>
          <div class="title">{{ item }}</div>
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M16 17l5-5-5-5M19.8 12H9M10 3H4v18h6"/></svg>
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
        </div></div>
        </li>
    </div>

</div>
</template>

<script>
export default {
     name: 'Card',
   data: function () {
     return {
        list: [
            "Video1",
            "Video2",
            "Video3",
            "Video4",
            "Video5",
            "Video6",
            "Video7"
        ]
     }
   },
computed: {
  groupedArray() {
    const base = this.list.length
    const split_cnt = 3       // 何個ずつに分割するか
    const grouped_list = []
    for (let i=0; i<Math.ceil(base/split_cnt); i++) {
      let multiple_cnt = i * split_cnt  // 3の倍数
      // (i * 3)番目から(i * 3 + 3)番目まで取得
      let result = this.list.slice(multiple_cnt, multiple_cnt + split_cnt) 
      grouped_list.push(result)
    }
    return grouped_list
    // [
    //   ["AMETHYST", "BLUE-SAPPHIRE", "CITRIN"],
    //   ["DIAMOND", "EMERALD", "FIRE-OPAL"], ...
    // ]
  }
}
}
</script>

<style scoped>
.card {
  width:82%;
  position: absolute;
  right: 0;
  margin-top: 50px;
}

.cards {
  width:300px;
  height:250px;
  margin: 20px 20px;
  display: inline-block;
  /* box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2); */
  border-radius: 3px;
}

.cards_inner {
  margin: 0 auto;
  width:95%;
  height:95%;
}

.upper_video {
  width:100%;
  height:60%;
  background-color:#F7F7F7;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
}

.lower_text {
  width:100%;
  height:40%;
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
</style>