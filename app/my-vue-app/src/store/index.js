import Vuex from 'vuex'
import Vue from 'vue'
import createPersistedState from "vuex-persistedstate";


Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      user:'',
    },
    mutations: {
        setUsername (state, input) {
          state.user = input
        }
    },
    plugins: [createPersistedState({storage: window.sessionStorage})]
  })

export default store