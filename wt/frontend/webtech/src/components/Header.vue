<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link id="design" to="/" class="nav-link">
            Home
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="design" to="/about" class="nav-link">
            About
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
</script>

<style>
#design{
  background: rgba(0, 0, 0, 0.2);
  margin:10px;
  border-radius: 10px;
  padding-right: 25px;
  padding-left: 25px;
}
</style>
