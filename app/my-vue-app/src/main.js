import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios' //追記
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify' 
import VueCookies from 'vue-cookies'

Vue.config.productionTip = false
console.log('fas')
Vue.use(VueAxios, axios)
Vue.use(Vuetify)
Vue.use(VueCookies)

new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
