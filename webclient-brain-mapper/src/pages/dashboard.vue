<template>
  <div class="px-8 py-10">
    <h3 class="text-xl">{{ $t('dashboard.title') }}</h3>
    <div>
      <v-row style="justify-content: space-around;" class="mt-5">
        <v-col
          cols="4" xl="4"
          v-for="card in filteredCards"
        >
          <v-card
            class="option-card"
            @click="navigate(card.url)"
            color="primary"
            variant="tonal"
            link
          >
            <v-card-text class="option-card-body">
              <v-icon :icon="card.icon"/>
              <span class="mt-2">{{ card.title }}</span>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<route lang="json">
  {
    "meta": {
      "layout": "default",
      "requiresAuth": false,
      "allowedRoles": [
        "ADMIN",
        "DATASET_MANAGER",
        "AI_USER",
        "AI_TECHNICIAN"
      ]
    }
  }
</route>

<script>
import { mapState } from 'pinia';
import { useAuthStore } from '@/stores/auth';

export default {
  name: 'Dashboard',

  data() {
    return {
      cards: [
        {
          title: this.$t('dashboard.users'),
          url: 'users',
          icon: 'mdi-account-group',
          requiredPermissions: 'isAdmin'
        },
        {
          title: this.$t('dashboard.dataset'),
          url: 'dataset',
          icon: 'mdi-database-arrow-up',
          requiredPermissions: 'datasetPermissionGranted'
        },
        {
          title: this.$t('dashboard.inferences'),
          url: 'inferences',
          icon: 'mdi-robot',
          requiredPermissions: 'inferencesPermissionGranted'
        }
      ]
    }
  },

  computed: {
    ...mapState(useAuthStore, {
      isAdmin: (store) => store.isAdmin,
      datasetPermissionGranted: (store) => store.datasetPermissionGranted,
      inferencesPermissionGranted: (store) => store.inferencesPermissionGranted,
    }),

    filteredCards() {
      return this.cards.filter(card => this.userHasAccess(card));
    }
  },

  methods: {
    // Check if user has enough permissions to show card(fast link)
    userHasAccess(card) {
      // Check if user is ADMIN
      if(this.isAdmin) return true;
      
      // Get the required permissions
      const requiredPermissions = card.requiredPermissions;

      // Check with the mapped getters if user permissions match required permissions
      // e.g if requiredPermissions = 'isAdmin', it will call this.isAdmin getter
      return this[requiredPermissions];
    },
    
    // Redirects user to certain section
    navigate(path) {
      this.$router.push({ path: `/${path}` });
    }
  }
};
</script>

<style lang="scss">
.option-card{
  margin-bottom: 3rem;
  height: 12rem;
	color: rgba(34,34,34,.7);
  span {
    font-size: 1.1rem;
  }
}

// .option-card:hover{
//   background-color: $secondary-hover-bgColor;
//   color: $secondary-hover-textColor;
//   border-color: $white-shade;
//   cursor: pointer;
// }

.option-card-body{
  display: flex;
  -ms-flex: 1 1 auto;
  -webkit-box-flex: 1;
  flex: 1 1 auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100%;
  padding: 1.25rem;

  i{
    font-size: 2rem !important;
  }
}
</style>