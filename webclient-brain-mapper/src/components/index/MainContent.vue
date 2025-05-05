<template>
	<div id="main-content">
		<!-- Intro block -->
		<section>
			<div class="grid max-w-screen-xl px-4 pt-20 pb-16 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 lg:pt-28">
				<div class="mr-auto place-self-center lg:col-span-7">
					<h1 class="max-w-2xl mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl xl:text-6xl">
						{{ $t('index.titlePt1') }}<br>{{ $t('index.titlePt2') }}
					</h1>
					<p class="max-w-2xl mb-6 font-light text-gray-600 lg:mb-8 md:text-lg lg:text-xl">
						{{ $t('index.description') }}
					</p>
				</div>
				<div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
					<img src="@/assets/hero_berrynet.png" alt="berrys image">
				</div>
			</div>
		</section>
		<!-- End of Intro block -->

		<!-- Start block -->
		<!-- Purposes -->
		<section id="purposes" class="bg-gray-50">
			<div class="max-w-screen-xl px-4 py-16 mx-auto space-y-12 lg:space-y-20 lg:py-24 lg:px-6">
				<div class="gap-8 lg:grid lg:grid-cols-2 xl:gap-16">
					<!-- Col 1 -->
					<div class="text-gray-600 sm:text-lg">
						<h2 class="mb-4 text-3xl font-extrabold tracking-tight text-gray-900">
							{{ $t('index.purposes') }}
						</h2>
						<p class="mb-8 font-light lg:text-xl">
							{{ $t('index.purposesDet') }}
						</p>
						<!-- List -->
						<ul role="list" class="pt-8 space-y-5 border-t border-gray-200 my-7">
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900">
									{{ $t('index.purpose1') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900">
									{{ $t('index.purpose2') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900 ">
									{{ $t('index.purpose3') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900 ">
									{{ $t('index.purpose4') }}
								</span>
							</li>
						</ul>
						<p class="mb-8 font-light lg:text-xl">
							{{ $t('index.purposesConclusion') }}
						</p>
					</div>

					<!-- Col 2 -->
					<img
						class="hidden w-full mb-4 rounded-lg lg:mb-0 lg:flex"
						src="@/assets/rotten-berry.webp"
						alt="roten_berry"
					>
				</div>
			</div>
		</section>
		<!-- End block -->

		<!-- Start block -->
		<!-- Critical challenges -->
		<section id="challenges" class="bg-gray-50">
			<div class="max-w-screen-xl px-4 py-16 mx-auto space-y-12 lg:space-y-20 lg:py-24 lg:px-6">
				<div class="gap-8 lg:grid lg:grid-cols-2 xl:gap-16">
					<!-- Col 1 -->
					<img
						class="hidden w-full mb-4 rounded-lg lg:mb-0 lg:flex"
						src="@/assets/invernadero-agricola.jpg"
						alt="dashboard feature image"
					>

					<!-- Col 2 -->
					<div class="text-gray-600 sm:text-lg">
						<!-- Subtitle -->
						<h2 class="mb-4 text-3xl font-extrabold tracking-tight text-gray-900">
							{{ $t('index.challenges') }}
						</h2>
						<!-- Description -->
						<p class="mb-8 font-light lg:text-xl">
							{{ $t('index.challengesDet') }}
						</p>
						<!--Challenges List -->
						<ul role="list" class="pt-8 space-y-5 border-t border-gray-200 my-7">
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900">
									{{ $t('index.challenge1') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900">
									{{ $t('index.challenge2') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900 ">
									{{ $t('index.challenge3') }}
								</span>
							</li>
							<li class="flex space-x-3">
								<!-- Icon -->
								<v-icon color="highlight" icon="mdi-check-circle" size="small"></v-icon>
								<span class="text-base font-medium leading-tight text-gray-900 ">
									{{ $t('index.challenge4') }}
								</span>
							</li>
						</ul>
						<p class="mb-8 font-light lg:text-xl">
							{{ $t('index.challengesConclusion') }}
						</p>
					</div>
				</div>
			</div>
		</section>
		<!-- End block -->

		<!-- Start block -->
		<!-- Technologies -->
		<section id="technologies" class="bg-white">
			<div class="max-w-screen-xl px-4 py-16 mx-auto">
				<!-- Subtitle -->
				<h2 class="mb-6 text-3xl font-extrabold tracking-tight text-gray-900">
					{{ $t('index.technologies') }}
				</h2>
				<!-- Description -->
				<p class="mb-10 font-light lg:text-xl">
					{{ $t('index.technologiesDet') }}
				</p>

				<!-- Technologies list -->
				<div class="grid grid-cols-2 gap-8 text-gray-500 sm:gap-12 sm:grid-cols-2 lg:grid-cols-4">
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/docker-logo.png" alt="docker">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/flask-logo.png" alt="flask" class="h-48">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/minio_logo.png" alt="minio">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/Nginx_logo.png" alt="nginx">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/nvidia-cuda-logo.png" alt="cuda" class="h-48">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/postgresql-logo.png" alt="postgresql">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/python-logo.png" alt="python">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/pytorch-logo.png" alt="pytorch">
					</a>
					<a href="#" class="flex items-center lg:justify-center h-24">
						<img src="../../assets/vue-logo.png" alt="vue">
					</a>
				</div>
			</div>
		</section>
		<!-- End block -->

		<!-- Start block -->
		<!-- Infrastructure -->
		<section id="infrastructure" class="bg-white">
			<div class="max-w-screen-xl px-4 py-16 mx-auto lg:px-6">
				<div class="max-w-screen-lg mb-8 mx-auto text-center lg:mb-12">
					<h2 class="mb-4 text-3xl font-extrabold tracking-tight text-gray-900">
            {{ $t('index.infrastructure') }}
          </h2>
					<p class="mb-5 font-light text-gray-500 sm:text-xl">
            {{ $t('index.infraDet') }}
          </p>
				</div>
				<div class="space-y-8 flex flex-col">
					<!-- Infra Card -->
					<div class="flex flex-col max-w-6xl p-6 mx-auto text-center text-gray-900 bg-white border border-gray-100 rounded-lg shadow xl:p-8">
						<h3 class="mb-4 text-2xl font-semibold">{{ $t('index.infraModular') }}</h3>
						<img src="../../assets/infra-modular.png" alt="infrastructureBase">
          </div>
          <!-- Infra Card -->
					<div class="flex flex-col max-w-6xl p-6 mx-auto text-center text-gray-900 bg-white border border-gray-100 rounded-lg shadow xl:p-8">
						<h3 class="mb-4 text-2xl font-semibold">{{ $t('index.infraMonolit') }}</h3>
						<img src="../../assets/infra-monolit.png" alt="infrastructureBase">
          </div>
				</div>
			</div>
		</section>
		<!-- End block -->

    <!-- Start block -->
		<!-- AI Model -->
		<section id="ai-model" class="bg-white">
			<div class="max-w-screen-xl px-4 py-16 mx-auto lg:px-6">
				<div class="max-w-screen-xl mb-8 mx-auto text-left lg:mb-12">
					<h2 class="mb-4 text-3xl font-extrabold tracking-tight text-gray-900">
            {{ $t('index.aiModel') }}
          </h2>
					<p class="mb-5 font-light text-gray-500 sm:text-xl">
            {{ $t('index.aiModelDet') }}
          </p>
				</div>
        <img src="../../assets/ai-model.png" alt="model" class="sm:p-6 lg:p-14 mx-auto">
			</div>
		</section>
		<!-- End block -->

    <!-- Start block -->
    <!-- Future work -->
    <section id="future-work" class="bg-white">
      <div class="max-w-screen-xl px-4 pt-16 pb-32 mx-auto lg:flex lg:flex-col lg:px-6">
        <div class="mb-8 text-left max-w-screen-xl">
          <h2 class="mt-3 mb-4 text-3xl font-extrabold tracking-tight text-gray-900 md:text-3xl">
            {{ $t('index.futureWork') }}
          </h2>
          <p class="font-light text-gray-500 sm:text-xl">
            {{ $t('index.futureWorkDet') }}
          </p>
        </div>
        <div class="flex flex-row justify-center pt-8">
          <div class="max-w-screen-lg md:grid md:grid-cols-2 md:gap-12 lg:grid-cols-3">
            <div>
              <v-icon color="highlight" icon="mdi-chart-box-plus-outline" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature1') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature1Det') }}</p>
            </div>
            <div>
              <v-icon color="highlight" icon="mdi-scale-unbalanced" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature2') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature2Det') }}</p>
            </div>
            <div>
              <v-icon color="highlight" icon="mdi-kubernetes" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature3') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature3Det') }}</p>
            </div>
            <div>
              <v-icon color="highlight" icon="mdi-map" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature4') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature4Det') }}</p>
            </div>
            <div>
              <v-icon color="highlight" icon="mdi-cctv" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature5') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature5Det') }}</p>
            </div>
            <div>
              <v-icon color="highlight" icon="mdi-fruit-watermelon" size="40px" class="mb-2 text-berry-highlight"></v-icon>
              <h3 class="mb-2 text-2xl font-bold ">{{ $t('index.feature6') }}</h3>
              <p class="font-light text-gray-500">{{ $t('index.feature6Det') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
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
