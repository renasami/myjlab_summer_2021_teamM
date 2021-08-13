<template>
<div>
    <ul id="card-list">
        <p>{{ message }}</p>
    </ul>
</div>
</template>

<script>
export default {
    name: 'Card',
  data: function () {
    return {
      message: "これはテストです"
    }
  }
}
</script>

<style scoped>

</style>