<template>
  <div>
    <h1>Minha Plataforma de Votação Descentralizada</h1>
    <button @click="fetchData">Buscar Dados do Backend</button>
    <div v-if="backendData">
      <p>Dados do Backend: {{ backendData }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backendData: null,
    };
  },
  methods: {
    async fetchData() {
      try {
        const response = await this.$axios.get('/endpoint-do-backend');
        this.backendData = response.data;
      } catch (error) {
        console.error('Erro ao buscar dados do backend', error);
      }
    },
  },
};
</script>

<style>
</style>
