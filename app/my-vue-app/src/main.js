import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
console.log('fas')

new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
