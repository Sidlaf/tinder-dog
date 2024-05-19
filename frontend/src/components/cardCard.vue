<script>
export default {
  name: 'cardCard',
  props: {
    Name: {
      type: String,
      required: true
    },
    Age: {
      type: String,
      required: true
    },
    Gender: {
      type: String,
      required: true
    },
    Description: {
      typr: String,
      required: true
    },
    Tag: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
  <div class="card">
    <div class="descrCard">
      <div class="allD">
        <div class="text1">
          <p style="font-size: 20px; color: white; font-weight: bold; margin-right: 8px">
            {{ Name }}
          </p>
          <p style="font-size: 20px; color: white">{{ Age }}</p>
        </div>
        <p style="font-size: 16px; color: white; margin-bottom: 8px">{{ Description }}</p>
        <div class="tags">
          <p
            style="
              margin-left: 12px;
              margin-right: 12px;
              margin-top: 3px;
              margin-bottom: 3px;
              text-decoration: underline;
              font-size: 13px;
            "
          >
            {{ Tag }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.card {
  background-image: url('../assets/image.png');
  background-size: cover;
  width: 353px;
  height: 514px;
  border-radius: 10px;
  display: flex;
  justify-content: left;
  align-items: end;
}
.allD {
  margin-top: 16px;
  margin-bottom: 16px;
  margin-left: 12px;
  margin-right: 12px;
}
.descrCard {
  margin-left: 16px;
  margin-bottom: 10px;
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}
.text1 {
  display: flex;
  justify-content: left;
  margin-bottom: 8px;
}
.tags {
  background-color: white;
  border: 1px solid;
  border-radius: 5px;
  border-color: black;
  width: fit-content;
  display: flex;
  justify-content: center;
}
</style>
