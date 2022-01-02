# Vue 3 + Typescript + Vite

This template should help get you started developing with Vue 3 and Typescript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)

## Type Support For `.vue` Imports in TS

Since TypeScript cannot handle type information for `.vue` imports, they are shimmed to be a generic Vue component type by default. In most cases this is fine if you don't really care about component prop types outside of templates. However, if you wish to get actual prop types in `.vue` imports (for example to get props validation when using manual `h(...)` calls), you can enable Volar's `.vue` type support plugin by running `Volar: Switch TS Plugin on/off` from VSCode command palette.

## Helpful reads on Vue
- [Best practices](https://learnvue.co/2020/01/12-vuejs-best-practices-for-pro-developers/#11-don-t-call-a-method-on-created-and-watch)
- [How computed properties work](https://learnvue.co/2019/12/mastering-computed-properties-in-vuejs/#ok-but-how-do-computed-properties-work)
- [Life cycle hooks](https://learnvue.co/2020/12/how-to-use-lifecycle-hooks-in-vue3/)
- [Global components](https://learnvue.co/2020/08/how-to-register-a-vue3-global-component/#what-are-vue-global-components)
- [V-model](https://learnvue.co/2021/01/everything-you-need-to-know-about-vue-v-model/)
- [Vue watch](https://learnvue.co/2020/03/a-simple-vue-watcher-tutorial-for-beginners/)
- [Vue Router](https://learnvue.co/2020/04/a-first-look-at-vue-router-in-vue3/)
- [Vue Keep-Alive](https://learnvue.co/2019/12/an-overview-of-vue-keep-alive/)

### Running our app locally
`npm install`
`npm run dev`
navigate to `http://localhost:3000/`, and you should see that it's running!

### Managing asset URLs
reference assets absolutely/relatively

- `absolutely`: assets referenced with `/file.extension` in the `public` folder will be coied to the root of the `dist` folder when project is built

- `relatively`: files in the `src/assets` folder are relatively accessed based on the file structure of the folder. This entire folder is placed as `_assets` in the `dist` folder when project is built

### Building for production
run `npm run build`, which calls `vite build`, which will bundle the Vlue project and prepare your dist folder to be served