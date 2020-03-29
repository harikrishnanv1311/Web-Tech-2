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
        <form v-on:submit.prevent="fetchData" class="form-group">
          <h4 class="jumbotron display-4">Enter the Topic of Papers To Be Recommended!</h4>
          <input id="forWidth" type="text" style="margin:5px; padding:5px;text-align:center;" placeholder="Type Here!" v-model="rec"><br>
          <br>
          <ul style="text-align:center">
            <li v-for="(p,index) in papers" :key="index">
              <div class="container">
                <div class="card text-center" style="text-align:center; width:100%; ">
                  <div class="card-body">
                    <h1 class="card-title"><b>{{p.name}}</b></h1>
                    <h6 class="card-subtitle mb-2 text-muted">{{p.author}}</h6>
                    <p class="card-text">HTML: <a v-bind:href="p.link_html">{{p.link_html}}</a><br>PDF: <a v-bind:href="p.link_pdf">{{p.link_pdf}}</a></p> 
                  </div>
                </div>
              </div>
            </li><br>
          </ul>
        </form>
        <p v-if="bool"> These are the papers available! </p>
      </div>
    </section>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'WT',
  data() {
    return {
      rec:"",
      bool:false,
      papers:[],
      users:[]
    }
  },
  // mounted: function(){
  //   axios.get('https://jsonplaceholder.typicode.com/posts')
  //     .then(response => console.log(response));
  // }
  methods: {
    fetchData: function(){
      this.bool=false;
      if(this.rec.length>0){
        console.log(this.rec.length);
        const baseURI = 'http://127.0.0.1:8000/getRecommendation/'+this.rec.replace(" ","-");
        console.log(baseURI);
        axios.get(baseURI).then(result => {
          this.papers=result.data;
          // this.papers=result.data.name+"\n"+result.data.author"\n"+result.data.links;
          console.log(this.papers);
          this.bool=true;
        })
      }

    }
  }

  // created() {
  //   setInterval(() => {
  //     this.fetchData()
  //   }, 2000)
  // }
}
</script>

<style>
#forWidth{
  width:60%;
  height: 50px;
  border-radius:15px;
}

</style>