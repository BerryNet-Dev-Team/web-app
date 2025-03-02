<template>
  <div id="main-content">
    <!-- Intro block -->
    <section>
      <div class="grid max-w-screen-xl px-4 pt-20 pb-16 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 lg:pt-28">
        <div class="mr-auto place-self-center lg:col-span-7">
          <h1 class="max-w-2xl mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl xl:text-6xl">
            Lorem ipsum 
            <br>lorem & ipsum.
          </h1>
          <p class="max-w-2xl mb-6 font-light text-gray-600 lg:mb-8 md:text-lg lg:text-xl">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus, excepturi, corrupti quas et nemo qui, perferendis asperiores magni possimus nam officia illo ad tempora aspernatur. Placeat explicabo quasi ab dolore!
          </p>
        </div>
        <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
          <img src="@/assets/BerryNetLogo.png" alt="berrys image">
        </div>
      </div>
    </section>
    <!-- End of Intro block -->

    <!-- Start block -->
    <section class="bg-gray-50">
      <div class="max-w-screen-xl px-4 py-16 mx-auto space-y-12 lg:space-y-20 lg:py-24 lg:px-6">
        <div class="items-center gap-8 lg:grid lg:grid-cols-2 xl:gap-16">
          <!-- Col 1 -->
          <div class="text-gray-600 sm:text-lg">
            <h2 class="mb-4 text-3xl font-extrabold tracking-tight text-gray-900">
              Lorem ipsum
            </h2>
            <p class="mb-8 font-light lg:text-xl">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Commodi nisi vitae, assumenda consequatur laborum excepturi a perspiciatis consectetur sint nostrum enim, nesciunt possimus ipsam officia provident quibusdam odio, deleniti voluptas!
            </p>
            <!-- List -->
            <ul role="list" class="pt-8 space-y-5 border-t border-gray-200 my-7">
              <li class="flex space-x-3">
                <!-- Icon -->
                <v-icon
                  color="highlight"
                  icon="mdi-check-circle"
                  size="small"
                ></v-icon>
                <span class="text-base font-medium leading-tight text-gray-900">
                  Lorem ipsum
                </span>
              </li>
              <li class="flex space-x-3">
                <!-- Icon -->
                <v-icon
                  color="highlight"
                  icon="mdi-check-circle"
                  size="small"
                ></v-icon>
                <span class="text-base font-medium leading-tight text-gray-900">
                  Lorem ipsum
                </span>
              </li>
              <li class="flex space-x-3">
                <!-- Icon -->
                <v-icon
                  color="highlight"
                  icon="mdi-check-circle"
                  size="small"
                ></v-icon>
                <span class="text-base font-medium leading-tight text-gray-900 ">
                  Lorem ipsum
                </span>
              </li>
            </ul>
            <p class="mb-8 font-light lg:text-xl">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil, sapiente consequatur sint iste pariatur rem! Distinctio voluptatum minima fuga voluptates sequi quidem neque natus voluptatem eum deserunt. Praesentium, magni veritatis.
            </p>
          </div>

          <!-- Col 2 -->
          <img class="hidden w-full mb-4 rounded-lg lg:mb-0 lg:flex" src="@/assets/grafica-ejemplo.webp" alt="dashboard feature image">
        </div>
      </div>
    </section>
    <!-- End block -->
  </div>
</template>

<script>

</script>

<style>
  #main-content {
    /* height: 100%; */
    width: 100%;
  }
</style>
