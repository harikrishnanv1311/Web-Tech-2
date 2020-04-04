<template>
  <div>
    <section class="hero is-dark">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Content-Based Research Paper Recommendation and Analytics Engine</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container" style="text-align:center;">
        <form v-on:keyup.prevent="fetchData" class="form-group">
          <h4 class="jumbotron display-4">Enter the Topic of Papers To Be Recommended!</h4>
          <input id="forWidth" type="text" style="margin:5px; padding:5px;text-align:center;" placeholder="Type Here!" v-model="rec"><br>
          <br>
          <ul style="text-align:center">
            <transition-group name="list" enter-class-active="animated bounceInUp" leave-active-class="animated bounceOutDown">
              <li v-if="showRec" v-for="(p,index) in papers" :key="p.name">
                <div class="container">
                  <div class="card text-center" style="text-align:center; width:100%; ">
                    <div class="card-body">
                      <h1 class="card-title"><b>{{p.name}}</b></h1>
                      <h6 class="card-subtitle mb-2 text-muted">{{p.author}}</h6>
                      <p class="card-text">HTML: <a v-bind:href="p.link_html">{{p.link_html}}</a><br>PDF: <a v-bind:href="p.link_pdf">{{p.link_pdf}}</a></p> 
                    </div>
                  </div>
                </div>
              </li>
            </transition-group>
          </ul>
        </form>
        <p v-if="bool"> These are the papers available! </p><br>
        <button class="btn btn-primary" v-if="showButton1" v-on:click.prevent="fetchYear">Get Year Stats</button>
        <button class="btn btn-primary" v-if="showButton2" v-on:click.prevent="fetchAuthor">Get Author Stats</button>

        <img id="imgSrc1" v-if="showImg1" style="margin:30px" v-bind:src="imgSrc1" alt="Loading ..."></img>
        <img id="imgSrc2" v-if="showImg2" style="margin:30px" v-bind:src="imgSrc2" alt="Loading ..."></img>
        
      </div>
    </section>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WT',
  data() {
    return {
      rec:"",
      showRec:false,
      bool:false,
      showButton1:false,
      showButton2:false,
      imgSrc1:"",
      imgSrc2:"",
      showImg1:false,
      showImg2:false,
      papers:[],
      users:[]
    }
  },
  // mounted: function(){
  //   this.$nextTick(function(){
  //     this.fetchYear().then(result => {
  //         console.log(result);
  //         const url = window.URL.createObjectURL(new Blob([result.data]));
  //         const link = document.createElement("img");
  //         link.src = url;
  //         document.getElementById("imgSrc1").src=link;
          
  //         // console.log(result.data);
  //         //this.imgSrc1=URL.createObjectURL(result);
  //       })
  //   })
  // },

  methods: {
      fetchData: function(){
      this.bool=false;
      this.showRec=false;
      this.showButton1=false;
      this.showButton2=false;
      this.showImg1=false;
      this.showImg2=false;
      if(this.rec.length>0){
        console.log(this.rec.length);
        const baseURI = 'http://127.0.0.1:8000/getRecommendation/'+this.rec.replace(" ","-");
        console.log(baseURI);
        axios.get(baseURI).then(result => {
          this.papers=result.data;
          // this.papers=result.data.name+"\n"+result.data.author"\n"+result.data.links;
          console.log(this.papers);
          this.showRec=true;
          this.bool=true;
          this.showButton1=true;
          this.showButton2=true;
        })
      }
    },

    fetchYear: function(){
      console.log("Received Year Signal!");   
      const baseURI = 'http://127.0.0.1:8000/getHistogram/year'; 
      return axios({
        url: baseURI,
        method: 'GET',
        responseType: 'blob', // important
      })
      .then(result => {
          console.log(result);
          const url = window.URL.createObjectURL(new Blob([result.data]));
          console.log(url);
          this.imgSrc1=url;
          this.showImg2=false;
          this.showImg1=true;
          this.showButton1=false;
          this.showButton2=true;
          
        })
    },

    fetchAuthor: function(){
      console.log("Received Author Signal!");   
      const baseURI = 'http://127.0.0.1:8000/getHistogram/author'; 
      return axios({
        url: baseURI,
        method: 'GET',
        responseType: 'blob', // important
      })
      .then(result => {
          console.log(result);
          const url = window.URL.createObjectURL(new Blob([result.data]));
          console.log(url);
          this.imgSrc2=url;
          this.showImg1=false;
          this.showImg2=true;
          this.showButton2=false;
          this.showButton1=true;
        })
    }

  }

  // .then(result => {
  //         console.log(result);
  //         const url = window.URL.createObjectURL(new Blob([result.data]));
  //         const link = document.createElement("img");
  //         link.src = url;
  //         console.log(link);
  //         this.imgSrc1=link;
  //         this.showButton=true;
  //         // console.log(result.data);
  //         //this.imgSrc1=URL.createObjectURL(result);
  //       })

  // created() {
  //   setInterval(() => {
  //     this.fetchData()
  //   }, 2000)
  // }
}

</script>
@import 'https://cdn.jsdelivr.net/npm/animate.css@3.5.1';

<style>
#forWidth{
  width:60%;
  height: 50px;
  border-radius:15px;
}

</style>