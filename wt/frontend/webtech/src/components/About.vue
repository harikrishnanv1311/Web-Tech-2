<template>
  <div class="container">
    <div class="container">
      <div class="about jumbotron">
        <slot>
            <h1 class="display-4" id="toGivePadding" style="text-align:center">Content-Based Research Paper Recommendation and Analytics Engine</h1>
            <p class="lead">At this time and age, research progresses exponentially and a lot of research papers get published everyday making it hard for a user to find a genuinely good research paper which is relevant to his/her field of research. We plan to solve this problem by analyzing research papers and providing the best papers relevant to the query of the user. We also provide relevant analytics related to the query as well as to each paper.</p>
            <p class="lead">We have used ARXIV data from 31000+ papers which is present on Kaggle. This data is mostly restricted to computer science. It contains metadata of all papers related to machine learning, computational language, neural and evolutionary computing, artificial intelligence, and computer vision fields published between 1992 to 2018.</p>
        </slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
#toGivePadding {
  margin: 40px;
  border-radius:15px;
  padding: 30px;
  background: darkgray;
  color: rgb(0, 0, 0);
}
</style>