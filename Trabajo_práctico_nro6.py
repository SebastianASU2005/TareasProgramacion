





<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"  data-a11y-animated-images="system" data-a11y-link-underlines="false">

    <style>
  /* for each iteration, uncomment the CSS variable */

  /* light themes */
  [data-color-mode="light"][data-light-theme*="light"],
  [data-color-mode="auto"][data-light-theme*="light"] {
    /* iteration 1 */
    --border-color-iteration-1: #C8CCD0;
    /* iteration 2 */
    --border-color-iteration-2: #BABFC5;
    /* iteration 3 */
    --border-color-iteration-3: #A6ADB4;
    /* iteration final */
    /* --border-color-iteration-4: #868F99; */

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  /* dark themes */
  [data-color-mode="dark"][data-dark-theme*="dark"],
  [data-color-mode="auto"][data-light-theme*="dark"] {
    /* iteration 1 */
    --border-color-iteration-1: #363940;
    /* iteration 2 */
    --border-color-iteration-2: #3F434B;
    /* iteration 3 */
    --border-color-iteration-3: #4B5159;
    /* iteration final */
    /* --border-color-iteration-4: #666E79; */

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  [data-color-mode="dark"][data-dark-theme="dark_dimmed"],
  [data-color-mode="dark"][data-dark-theme="light_high_contrast"],
  [data-color-mode="dark"][data-dark-theme="dark_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_dimmed"],
  [data-color-mode="light"][data-light-theme="light_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_high_contrast"] {
    /* skip these themes, use the fallback */
    --control-borderColor-rest: initial !important;
  }

  @media (prefers-color-scheme: dark) {
    /* dark colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      /* --border-color-iteration-4: #666E79; */

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      /* --border-color-iteration-4: #868F99; */

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
      }

    [data-color-mode="auto"][data-dark-theme="dark_dimmed"],
    [data-color-mode="auto"][data-dark-theme="light_high_contrast"],
    [data-color-mode="auto"][data-dark-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }

  @media (prefers-color-scheme: light) {
    /* dark colors in light mode */
    [data-color-mode="auto"][data-light-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      /* --border-color-iteration-4: #666E79; */

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in light mode */
    [data-color-mode="auto"][data-light-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      /* --border-color-iteration-4: #868F99; */

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    [data-color-mode="auto"][data-light-theme="dark_dimmed"],
    [data-color-mode="auto"][data-light-theme="light_high_contrast"],
    [data-color-mode="auto"][data-light-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }
</style>


  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-b92e9647318f.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-5d486a4ede8e.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-27c8d635e4e5.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-8438e75afd36.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-bf5665b96628.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-c414b5ba1dce.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-e5868b7374db.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-299ac9c64ec0.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-3a26e78ad0ff.css" />
  
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-d6dcdf72e61d.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-faa25eb56e2e.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-933ef5369a60.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-71ecd5638fbf.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["failbot_handle_non_errors","geojson_azure_maps","hovercard_show_on_focus","image_metric_tracking","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","star_button_focus"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-ab4b48c67ba1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/environment-fc6543d75794.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-3485f2997bc6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-981cc2eaa259.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-464f50283c96.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-6bd50a0647d6.js"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-210c4b5934c3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-cf03673d2172.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Box_Box_js-96a44addc402.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_Button_js-node_modules_primer_react_lib-esm_-f6da63-1976b80d3486.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_js-03b6dd82d40a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_index_js-node_modules_primer_react_lib-esm_O-701f13-047a44a18d3a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-0f28951279b7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-535c8ee1ebe8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-2f08ef908241.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-04bb1b-a6096689d2d5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-9b048a5a5ceb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_react-router-dom_dist_index_js-4a785319b497.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-7693f4e3427d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-ad64b6-f3217651e114.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav2_index_js-b739f40cf454.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-9bd36c-c9a87fd5afd0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-6d3540-684005f5bdbe.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Breadcrumbs_Breadcrumbs_js-node_modules_primer_reac-31943d-f0539d68eb2b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-1ee1e572fd0e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_register-app_ts-afd2d748b726.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_ref-selector_RefSelector_tsx-bd2f6d26f4a6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-681869-f63e0555b81f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-cc11d2-b952d9af4c18.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-58ad5d5611fd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-b3d664d404df.js"></script>


  <title>Programacion1/Trabajo_práctico_nro6.py at main · paulog16/Programacion1</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)">

    
  <meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7">


  <meta name="request-id" content="F2F1:8B229:E18336:F3E547:6529A954" data-turbo-transient="true" /><meta name="html-safe-nonce" content="89674ea063deec1174892c5c1e989fcadaaf8e92cadb2ed8a2fb5ec7455a4e99" data-turbo-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9wYXVsb2cxNi9Qcm9ncmFtYWNpb24xIiwicmVxdWVzdF9pZCI6IkYyRjE6OEIyMjk6RTE4MzM2OkYzRTU0Nzo2NTI5QTk1NCIsInZpc2l0b3JfaWQiOiI1NzU4MTIwMjUxNTA4NTg2NjEyIiwicmVnaW9uX2VkZ2UiOiJicmF6aWxzb3V0aCIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient="true" /><meta name="visitor-hmac" content="90ad445f1937f8996ad16ebd809485d870f96242ec7085b8f9318605a3027992" data-turbo-transient="true" />


    <meta name="hovercard-subject-tag" content="repository:676124202" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
  <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" /><meta name="octolytics-actor-id" content="142347931" /><meta name="octolytics-actor-login" content="SebastianASU2005" /><meta name="octolytics-actor-hash" content="ba91c7e03090e2e77c7639ca6b84030e5a3674e04296b830102ba363c990b69a" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




  

    <meta name="user-login" content="SebastianASU2005">

  <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="Contribute to paulog16/Programacion1 development by creating an account on GitHub.">
      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py" />
      <meta name="twitter:image:src" content="https://opengraph.githubassets.com/23f1826daec6192815335c140a0068030360c081177c31f2d01f4fa2b6a3bad6/paulog16/Programacion1" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="Programacion1/Trabajo_práctico_nro6.py at main · paulog16/Programacion1" /><meta name="twitter:description" content="Contribute to paulog16/Programacion1 development by creating an account on GitHub." />
      <meta property="og:image" content="https://opengraph.githubassets.com/23f1826daec6192815335c140a0068030360c081177c31f2d01f4fa2b6a3bad6/paulog16/Programacion1" /><meta property="og:image:alt" content="Contribute to paulog16/Programacion1 development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="Programacion1/Trabajo_práctico_nro6.py at main · paulog16/Programacion1" /><meta property="og:url" content="https://github.com/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py" /><meta property="og:description" content="Contribute to paulog16/Programacion1 development by creating an account on GitHub." />
      

      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/142347931/ws?session=eyJ2IjoiVjMiLCJ1IjoxNDIzNDc5MzEsInMiOjEyMTY1ODI4MzgsImMiOjM5NDY0MDkwMDAsInQiOjE2OTcyMjkxNDN9--2587bda3d8ecc5376b3c6d67b04524ad7c3eab9831780ca67b87c34e6fd560c2" data-refresh-url="/_alive" data-session-id="fac1391864d400625bf41343645344c4b74af6760a1b2932dd442975f4334ef4">
      <link rel="shared-web-socket-src" href="/assets-cdn/worker/socket-worker-cee473359cfe.js">


        <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="a0cedc154d037e4a0a80601ce548731d6ad09a75f943eca9788b9c21e9896367" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ee14a7165914197d62e19f664bfb961fcfdfc1ec31939a5c7b137fbab1751c87" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="206b919dd058babca1d574c4b804030c6c17c2f6fb9c18590ef364a71ab7f2ee" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="532a9643051e7a4d0958924fb8f055b565c8cd3f5679d9de99d276f401f12c7e" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>
    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/paulog16/Programacion1 git https://github.com/paulog16/Programacion1.git">

  <meta name="octolytics-dimension-user_id" content="123969047" /><meta name="octolytics-dimension-user_login" content="paulog16" /><meta name="octolytics-dimension-repository_id" content="676124202" /><meta name="octolytics-dimension-repository_nwo" content="paulog16/Programacion1" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="676124202" /><meta name="octolytics-dimension-repository_network_root_nwo" content="paulog16/Programacion1" />



  <meta name="turbo-body-classes" content="logged-in env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
    <div data-turbo-body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


      

        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-b38cad-fb30c470f64b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-4db36910a4bc.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-00e5140a09e8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/command-palette-46bb1d1be80b.js"></script>

            <header class="AppHeader">
    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global">
  <include-fragment data-target="deferred-side-panel.fragment">
      
  <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e" id="dialog-show-dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-left" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e-title" aria-describedby="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-8d2cddad-1eee-4378-be2d-feebc5f4f79e" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">      <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-34e4d32d-3a93-409c-a7d4-6e39f005f742" href="/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-d44b5ed0-85e3-4edb-81a2-53ad4f2d4209" href="/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-8f7ae93a-49e7-4a8a-91fa-abb274475a28" href="/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-ea2de547-552a-41c0-a939-f5f0f869eb5b" href="/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-25734265-3463-4da6-920b-932b365887c4" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-71ff80bf-c060-4fb6-909d-997b1f3bdb8e" href="/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-24a7f55b-99e7-4ae7-8600-2e0a55fcbae7" href="/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

      <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
        <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</div>
</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd d-block pt-0">      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider mt-0 mb-1"></li>

        <nav aria-label="Additional navigation" data-view-component="true" class="ActionList px-0 flex-1">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;FEEDBACK&quot;,&quot;label&quot;:null}" id="item-9f70f513-3607-430a-9f28-88a996b4c285" href="https://gh.io/navigation-update" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Give new navigation feedback
</span>        <span class="ActionListItem-visual ActionListItem-visual--trailing">
          <span title="Beta" data-view-component="true" class="Counter color-bg-default color-border-success-emphasis color-fg-success">Beta</span>
        </span>
</a>
  
  
</li>

</ul>  </nav-list>
</nav>

      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">&copy; 2023 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex text-small text-light">
          <a target="_blank" href="/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="/security" data-view-component="true" class="Link mr-2">Security</a>
        <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>
</div></div>
</div>
</modal-dialog></div>

  </include-fragment>
</deferred-side-panel>

        <a
          class="AppHeader-logo ml-2"
          href="https://github.com/"
          data-hotkey="g d"
          aria-label="Homepage "
          data-turbo="false"
          data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
        >
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context" >
  <div class="AppHeader-context-compact">
        <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: paulog16 / Programacion1" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">    <span class="Button-content">
      <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">paulog16</span>
                <span class="AppHeader-context-compact-separator">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate" >
  <span class="Truncate-text ">Programacion1</span>

</strong></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog role="dialog" id="context-region-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;paulog16&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/paulog16" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          paulog16
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Programacion1&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/paulog16/Programacion1" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          Programacion1
        </span>

</a>
    </li>
</ul>

</div>
      
</modal-dialog></div>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;paulog16&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/paulog16/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/paulog16" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          paulog16
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Programacion1&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="/paulog16/Programacion1" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          Programacion1
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search" >
              


<qbsearch-input class="search-input" data-scope="repo:paulog16/Programacion1" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="MSpfBnbK3eHcmLCZlziNgXz1dVAUOjL3VEo5PvoiCXqvHLzp7wDL27SbJ8GStkTJNRQNSc5eherKb6vecOpKMg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="paulog16/Programacion1" data-current-org="" data-current-owner="paulog16" data-logged-in="true">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label
        for="AppHeader-searchInput"
        aria-label="Search or jump to…"
        class="AppHeader-search-visual--leading"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button
            type="button"
            data-target="qbsearch-input.inputButton"
            data-action="click:qbsearch-input#handleExpand"
            class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap"
            data-hotkey="s,/"
            data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}"
          >
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-ba4145b4-2e38-4988-9da9-6fc729c14f33" for="AppHeader-commandPalette-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-05e193a1-aad6-467b-97e7-00073db6aa0c" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          
  <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>  

      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

        <div class="position-relative">
                <ul
                  role="listbox"
                  class="ActionListWrap QueryBuilder-ListWrap"
                  aria-label="Suggestions"
                  data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  "
                  data-target="query-builder.resultsList"
                  data-persist-list=false
                  id="query-builder-test-results"
                ></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-05e193a1-aad6-467b-97e7-00073db6aa0c" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
                <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">    <span class="Button-content">
      <span class="Button-label">Give feedback</span>
    </span>
</button>  
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="i7a_edJZer_y9bZzupfYRUI0rj4Ep49pm8-wUJVlcsnwEMerzaerqUtU6rdpYluVbm_rY3kLKfY1ODRv2Y5EVA" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</modal-dialog></div>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="_ZYTqIeZJwlrzq7NKGWb0kLfI1ZXQVBCocBY_eilijbW5DDuK8HjpF1cw836JO6MiAaqFNtZp6hPrhE_PPnr6w" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" value="GtUSvsICDTtOduhY9DK5BRSCjEdfJQVn8W73LEwgfiCQab14w7MtNR7-9898g6zixjhHEzqHEinJyZ1uo80s6A" data-csrf="true" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</modal-dialog></div>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="DIAiNMawdvihAe2ii4JFzJN4tmIsuh9wV8ZASaH6yZpMyh9LkF1KcbgdQr6O7NmuR9YM0G-sW7dZeGyGBOjfUA" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />

          </div>

        <div class="AppHeader-actions position-relative">
          <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <div data-view-component="true" class="Button-withTooltip">  <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted">    <span class="Button-content">
        <span class="Button-visual Button-leadingVisual">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
        </span>
      <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
    </span>
</button>  <tool-tip id="tooltip-f12ac120-fd57-4964-baae-1da2d341a8a3" for="global-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Create new...</tool-tip>
</div>

<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      
        <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new" tabindex="-1" id="item-15421b8c-1c27-421f-aed7-1044f1f2cd14" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new/import" tabindex="-1" id="item-cf23f0ab-796f-45be-b4aa-74c3b373e92f" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/codespaces/new" tabindex="-1" id="item-b9db410b-39d6-4782-8373-9b05ceb2d5ab" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-fdfbf97e-d706-4dd6-8ed6-8de7b519552a" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/account/organizations/new" tabindex="-1" id="item-3b611bcc-49b3-428a-b879-5e0d515a958a" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div></anchored-position>  </focus-group>
</action-menu>

          <div data-view-component="true" class="Button-withTooltip">
  <a href="/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-7da6d1c8-6420-4e77-b19f-70a2bf6f12be" aria-labelledby="tooltip-935474ad-0c03-497b-a2e3-0e6fe586d388" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-935474ad-0c03-497b-a2e3-0e6fe586d388" for="icon-button-7da6d1c8-6420-4e77-b19f-70a2bf6f12be" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Issues</tool-tip>
</div>
          <div data-view-component="true" class="Button-withTooltip">
  <a href="/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-f28c1994-8b84-49f2-8042-0bae06e94ed1" aria-labelledby="tooltip-bfa55197-7150-496d-a955-35e2bf723aa3" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-bfa55197-7150-496d-a955-35e2bf723aa3" for="icon-button-f28c1994-8b84-49f2-8042-0bae06e94ed1" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Pull requests</tool-tip>
</div>
          <div style="left: -205px; top: 34px;" data-view-component="true" class="js-notice Popover position-absolute d-none d-sm-none d-md-block d-lg-block">
  <div data-view-component="true" class="Popover-message Box Popover-message--top-right Popover-message--large p-4 mt-2 mx-auto text-left color-shadow-large">
    <h4 data-view-component="true" class="f5 mb-2">    Issues and Pull Requests
</h4>
        Now available from the navigation bar for immediate access everywhere.

    <div class="mt-3">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="js-notice-dismiss" data-turbo="false" action="/settings/dismiss-notice/global_nav_button_onboarding" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="_kjBh2kGopwSaPr7kf7TYmVASDCcLbIFfU42G6hr_5Ba3zvqwFrVyXUhf1Bxepn4XtcSLdL99ra_BlibqkBfog" autocomplete="off" />
          <button type="submit" data-view-component="true" class="Button--secondary Button--small Button">    <span class="Button-content">
      <span class="Button-label">Okay, got it!</span>
    </span>
</button>  

</form>    </div>

</div></div>
        </div>

        

<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTQyMzQ3OTMxIiwidCI6MTY5NzIyOTE0M30=--c1761cee3d72a309539611b98187b4764702c120a6105dd2c3be0c37f858d234" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel">
  <a id="AppHeader-notifications-button" href="/notifications"
    class="AppHeader-button Button--secondary"

    style="width:32px;height:32px;"

    data-hotkey="g n"
    data-target="notification-indicator.link"
    aria-label="Notifications"

      data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;notifications&quot;,&quot;label&quot;:null}"
  >

    <span
      data-target="notification-indicator.badge"
      class="mail-status unread d-none" hidden>
    </span>

      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox color-fg-muted mr-0">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
  </a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-ef922f7e-d8e8-4ced-9665-38460dee4436" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?memex_enabled=true&amp;repository=Programacion1&amp;user=SebastianASU2005&amp;user_can_create_organizations=true&amp;user_id=142347931">
  <include-fragment data-target="deferred-side-panel.fragment">
      <user-drawer-side-panel>
      <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e" id="dialog-show-dialog-29f69133-af7c-4fa0-9f32-585ce140e03e" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">    <span class="Button-content">
      <span class="Button-label"><img src="https://avatars.githubusercontent.com/u/142347931?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" /></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-right" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e-title" aria-describedby="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="https://avatars.githubusercontent.com/u/142347931?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" />
</div>        <div data-view-component="true" class="overflow-hidden d-flex width-full">        <div data-view-component="true" class="lh-condensed overflow-hidden d-flex flex-column flex-justify-center ml-2 f5 mr-auto width-full">
          <span data-view-component="true" class="Truncate text-bold">
    <span data-view-component="true" class="Truncate-text">
            SebastianASU2005
</span>
</span>          </div>
</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-29f69133-af7c-4fa0-9f32-585ce140e03e" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">      <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-b2eb746e-8118-4ee4-9a01-0e121530fb5c" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROFILE&quot;,&quot;label&quot;:null}" id="item-75cb0356-91bd-4f3a-b31c-e7ee8c810f99" href="https://github.com/SebastianASU2005" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-a9563713-5e12-45c8-8f71-4946e4cce08a" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;label&quot;:null}" id="item-3f3726ec-9040-453d-9d41-e8257f8ff48b" href="/SebastianASU2005?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_PROJECTS&quot;,&quot;label&quot;:null}" id="item-52a3b055-c634-4bf0-8cc6-c0072e80aaeb" href="/SebastianASU2005?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-90fcc41d-c772-492e-8a48-644edb05996d" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_STARS&quot;,&quot;label&quot;:null}" id="item-c42487c2-4cb6-4c32-bedb-aafc597f2361" href="/SebastianASU2005?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SPONSORS&quot;,&quot;label&quot;:null}" id="item-07b6d832-9e45-4c17-ac6d-c430a79f1bd7" href="/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_GISTS&quot;,&quot;label&quot;:null}" id="item-ab0db89c-2fd4-4341-be1d-c79202d9a80a" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-331f27b3-43b4-42f4-95f2-48c5ae6688c8" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-4a9ae3ce-7faf-4b03-8eb1-40507232c9de" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-7025a546-0128-4991-b9e5-dc33540aaf16" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SETTINGS&quot;,&quot;label&quot;:null}" id="item-7bef5c4e-c8a4-41e2-8d51-4e45381ba2d4" href="/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DOCS&quot;,&quot;label&quot;:null}" id="item-df87f177-3ab3-4f2c-b017-fe7195f0adef" href="https://docs.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SUPPORT&quot;,&quot;label&quot;:null}" id="item-9c9404ac-3379-43d9-9b71-5dee189c531f" href="https://support.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;LOGOUT&quot;,&quot;label&quot;:null}" id="item-63049173-e130-4208-9c7a-b33130244930" href="/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
      
</modal-dialog></div>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu>

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar" >
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/paulog16/Programacion1" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /paulog16/Programacion1" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/paulog16/Programacion1/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /paulog16/Programacion1/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/paulog16/Programacion1/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /paulog16/Programacion1/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/paulog16/Programacion1/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /paulog16/Programacion1/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/paulog16/Programacion1/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /paulog16/Programacion1/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/paulog16/Programacion1/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /paulog16/Programacion1/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/paulog16/Programacion1/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/paulog16/Programacion1/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /paulog16/Programacion1/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">        <details data-view-component="true" class="details-overlay details-reset position-relative">
    <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
    <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
          <ul>
              <li data-menu-item="i0code-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /paulog16/Programacion1" href="/paulog16/Programacion1">
                  Code
</a>              </li>
              <li data-menu-item="i1issues-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /paulog16/Programacion1/issues" href="/paulog16/Programacion1/issues">
                  Issues
</a>              </li>
              <li data-menu-item="i2pull-requests-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /paulog16/Programacion1/pulls" href="/paulog16/Programacion1/pulls">
                  Pull requests
</a>              </li>
              <li data-menu-item="i3actions-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /paulog16/Programacion1/actions" href="/paulog16/Programacion1/actions">
                  Actions
</a>              </li>
              <li data-menu-item="i4projects-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /paulog16/Programacion1/projects" href="/paulog16/Programacion1/projects">
                  Projects
</a>              </li>
              <li data-menu-item="i5security-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /paulog16/Programacion1/security" href="/paulog16/Programacion1/security">
                  Security
</a>              </li>
              <li data-menu-item="i6insights-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /paulog16/Programacion1/pulse" href="/paulog16/Programacion1/pulse">
                  Insights
</a>              </li>
          </ul>
</details-menu>
</details></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <div data-view-component="true" class="flash-close">
  <button id="icon-button-b9436acf-5a72-41ce-8d96-aef37c6d065a" aria-labelledby="tooltip-4c622767-4b0c-4ed3-83c8-bbfe6d5e9b9b" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium js-flash-close">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>  <tool-tip id="tooltip-4c622767-4b0c-4ed3-83c8-bbfe6d5e9b9b" for="icon-button-b9436acf-5a72-41ce-8d96-aef37c6d065a" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>
</div>

  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace>





  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div class="px-2" >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTQyMzQ3OTMxIiwidCI6MTY5NzIyOTE0M30=--c1761cee3d72a309539611b98187b4764702c120a6105dd2c3be0c37f858d234" data-view-component="true" class="js-socket-channel"></notification-shelf-watcher>
  <div hidden data-initial data-target="notification-shelf-watcher.placeholder"></div>






      <details
  class="details-reset details-overlay details-overlay-dark js-command-palette-dialog"
  id="command-palette-pjax-container"
  data-turbo-replace
>
  <summary aria-label="Command palette trigger" tabindex="-1"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="Command palette">
    <command-palette
      class="command-palette color-bg-default rounded-3 border color-shadow-small"
      return-to=/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py
      user-id="142347931"
      activation-hotkey="Mod+k,Mod+Alt+k"
      command-mode-hotkey="Mod+Shift+k"
      data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      ">

        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search issues and pull requests"
        ></command-palette-mode>
        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search issues, pull requests, discussions, and projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="!"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to a user, organization, or repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to a repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="/"
            data-scope-types="[&quot;repository&quot;]"
            data-placeholder="Search files"
        ></command-palette-mode>
        <command-palette-mode
          data-char="?"
        ></command-palette-mode>
        <command-palette-mode
          data-char="&gt;"
            data-placeholder="Run a command"
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
      <command-palette-mode
        class="js-command-palette-default-mode"
        data-char=""
        data-placeholder="Search or jump to..."
      ></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..."

        data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        "
      >
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden>
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle
              cx="8"
              cy="8"
              r="7"
              stroke="currentColor"
              stroke-opacity="0.25"
              stroke-width="2"
              vector-effect="non-scaling-stroke"
            ></circle>
            <path
              d="M15 8a7.002 7.002 0 00-7-7"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              vector-effect="non-scaling-stroke"
            ></path>
          </svg>
        </div>
        <command-palette-scope >
          <div data-target="command-palette-scope.placeholder" hidden class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token
                data-text="paulog16"
                data-id="U_kgDOB2OeFw"
                data-type="owner"
                data-value="paulog16"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >paulog16<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token
                data-text="Programacion1"
                data-id="R_kgDOKEzWKg"
                data-type="repository"
                data-value="Programacion1"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >Programacion1<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input
            class="js-overlay-input typeahead-input d-none"
            disabled
            tabindex="-1"
            aria-label="Hidden input for typeahead"
          >
          <input
            type="text"
            autocomplete="off"
            autocorrect="off"
            autocapitalize="off"
            spellcheck="false"
            class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator"
            aria-label="Command palette input"
            aria-haspopup="listbox"
            aria-expanded="false"
            aria-autocomplete="list"
            aria-controls="command-palette-page-stack"
            role="combobox"
            data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            "
          >
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-cadec9b7-bdb1-407a-a825-c124663c779b" for="command-palette-clear-button" popover="manual" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute">Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack
        data-default-scope-id="R_kgDOKEzWKg"
        data-default-scope-type="Repository"
        data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons"
      >
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error>
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty data-scope-types="*" data-match-mode="[^?]|^$">
          No results matched your search
        </command-palette-tip>

        <div hidden>

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group
              data-group-id="top"
              data-group-title="Top result"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="0"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="commands"
              data-group-title="Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}"
              data-default-priority="1"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="global_commands"
              data-group-title="Global Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}"
              data-default-priority="2"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="this_page"
              data-group-title="This Page"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="3"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="files"
              data-group-title="Files"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="4"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="default"
              data-group-title="Default"
              data-group-hint=""
              data-group-limits="{&quot;static_items_page&quot;:50}"
              data-default-priority="5"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="pages"
              data-group-title="Pages"
              data-group-hint=""
              data-group-limits="{&quot;repository&quot;:10}"
              data-default-priority="6"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="access_policies"
              data-group-title="Access Policies"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="7"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="organizations"
              data-group-title="Organizations"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="8"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="repositories"
              data-group-title="Repositories"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="9"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="references"
              data-group-title="Issues, pull requests, and discussions"
              data-group-hint="Type # to filter"
              data-group-limits="{}"
              data-default-priority="10"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="teams"
              data-group-title="Teams"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="11"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="users"
              data-group-title="Users"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="12"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="memex_projects"
              data-group-title="Projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="13"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="projects"
              data-group-title="Projects (classic)"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="14"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="footer"
              data-group-title="Footer"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="15"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="modes_help"
              data-group-title="Modes"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="16"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="filters_help"
              data-group-title="Use filters in issues, pull requests, discussions, and projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="17"
            >
            </command-palette-item-group>

            <command-palette-page
              data-page-title="paulog16"
              data-scope-id="U_kgDOB2OeFw"
              data-scope-type="owner"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
            <command-palette-page
              data-page-title="Programacion1"
              data-scope-id="R_kgDOKEzWKg"
              data-scope-type="repository"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
        </div>

        <command-palette-page data-is-root>
        </command-palette-page>
          <command-palette-page
            data-page-title="paulog16"
            data-scope-id="U_kgDOB2OeFw"
            data-scope-type="owner"
          >
          </command-palette-page>
          <command-palette-page
            data-page-title="Programacion1"
            data-scope-id="R_kgDOKEzWKg"
            data-scope-type="repository"
          >
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements"></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements">
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="@"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="!"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="/"
              data-scope-types="[&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="&gt;"
          >
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:pr"
          >
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:issue"
          >
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:discussion"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:project"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:open"
          >
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider
          data-type="commands"
          data-fetch-debounce="0"
            data-src="/command_palette/commands"
          data-supported-modes="[]"
            data-supports-commands
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_page_navigation"
          data-supported-modes="[&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to_members_only"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_members_only_prefetched"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="files"
          data-fetch-debounce="0"
            data-src="/command_palette/files"
          data-supported-modes="[&quot;/&quot;]"
            data-supported-scope-types="[&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/discussions"
          data-supported-modes="[&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/projects"
          data-supported-modes="[&quot;#&quot;,&quot;!&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/recent_issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/teams"
          data-supported-modes="[&quot;@&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/name_with_owner_repository"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
    </command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path
          fill="#959da5"
          d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"
        />
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      
      






    
  <div id="repository-container-header" data-turbo-replace hidden></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Alt+Meta+≥,Control+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Alt+Meta+≤,Control+Alt+," target="_blank" href="/codespaces/new/paulog16/Programacion1/tree/main?resume=1">Open in codespace</a>



    
      
    





<react-app
  app-name="react-code-view"
  initial-path="/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py"
  style="min-height: calc(100vh - 62px)"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"Trabajo_practico_5","path":"Trabajo_practico_5","contentType":"directory"},{"name":"Ejercicio Complementario1.py","path":"Ejercicio Complementario1.py","contentType":"file"},{"name":"Ejercicios en clase – Variables dimensionadas.py","path":"Ejercicios en clase – Variables dimensionadas.py","contentType":"file"},{"name":"Trabajo Práctico Nro 1 -Programación 1 - (2) (2).docx","path":"Trabajo Práctico Nro 1 -Programación 1 - (2) (2).docx","contentType":"file"},{"name":"Trabajo-Practico-n2.py","path":"Trabajo-Practico-n2.py","contentType":"file"},{"name":"Trabajo_Practico_Nro1_Parte2_Programacion.py","path":"Trabajo_Practico_Nro1_Parte2_Programacion.py","contentType":"file"},{"name":"Trabajo_práctico_nro6.py","path":"Trabajo_práctico_nro6.py","contentType":"file"},{"name":"ahorcado.py","path":"ahorcado.py","contentType":"file"},{"name":"ejercicio_ciclos.py","path":"ejercicio_ciclos.py","contentType":"file"},{"name":"ejercicio_clase_variables_dimensionales.py","path":"ejercicio_clase_variables_dimensionales.py","contentType":"file"},{"name":"funciones.py","path":"funciones.py","contentType":"file"},{"name":"repaso.py","path":"repaso.py","contentType":"file"},{"name":"repaso2.py","path":"repaso2.py","contentType":"file"},{"name":"tp_funciones.py","path":"tp_funciones.py","contentType":"file"},{"name":"trabajo-condicionales.py","path":"trabajo-condicionales.py","contentType":"file"},{"name":"trabajo_Practico3.py","path":"trabajo_Practico3.py","contentType":"file"},{"name":"trabajo_practico_nro4.py","path":"trabajo_practico_nro4.py","contentType":"file"}],"totalCount":17}},"fileTreeProcessingTime":1.602829,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":676124202,"defaultBranch":"main","name":"Programacion1","ownerLogin":"paulog16","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-08-08T10:38:20.000-03:00","ownerAvatar":"https://avatars.githubusercontent.com/u/123969047?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1693923541.0","canEdit":true,"refType":"branch","currentOid":"8b9c1f44ad03bd539d3786ab1ca31c20d91dbac3"},"path":"Trabajo_práctico_nro6.py","currentUser":{"id":142347931,"login":"SebastianASU2005","userEmail":"elneppon2005@gmail.com"},"blob":{"rawLines":["","\"\"\"1.\tSolicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.\"\"\"","list_number=[]","while True:","    num=int(input('ingrese numeros, ingrese 0 para finalizar:\\n'))","    if num!=0:","        list_number.append(num)","    if num==0:","        break","print(list_number)","\"\"\"2.\tA continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.\"\"\"","number=int(input('ingrese numero que quiera eliminar:\\n'))","if number in list_number:","    list_number.remove(number)","else:","    print('no hay coincidencias')                ","print(list_number)","#3.\tImprimir la sumatoria de todos los números de la lista.","suma=0","for i in list_number:","    suma+=i","print(f'la suma es: {suma}')    ","#4.\tSolicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.","other_number=int(input('ingrese un numero: '))","other_lista=[]","for i in list_number:","    if i\u003cother_number:","        other_lista.append(i)","for i in other_lista:","    print(i)","#5.\tGenerar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]","listanueva=[]","tupla=()","for i in list_number:","    cont=0","    for k in list_number:","        if i ==k:","            cont+=1","            tupla=(i,cont)","    listanueva.append(tupla)   ","","listaset=set(listanueva)            ","print(listaset)","    ","#6.\tSolicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.","","","","listanombresPrimaria=[]","listanombresSecundaria=[]","while True:","    nombresp=input('ingrese nombres de primaria, para finalizar ingrese X:\\n')","    if nombresp!='x':","        listanombresPrimaria.append(nombresp)","    if nombresp=='x':","        break","while True:","    nombress=input('ingrese nombres de secundaria, para finalizar ingrese X:\\n')","    if nombress!='x':","        listanombresSecundaria.append(nombress)","    if nombress=='x':","        break","#a.\tInformar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.    ","todoslosnombres=listanombresPrimaria+listanombresSecundaria","nombressinrepetir=set(todoslosnombres)","print(nombressinrepetir)","","#b.\tInformar qué nombres se repiten entre los alumnos de nivel primario y secundario.","nombresrepetidos=[]","nombresnorepetidos=[]","for i in listanombresPrimaria:","    for k in listanombresSecundaria:","        if i==k:","            nombresrepetidos.append(i)","        #c.\tInformar qué nombres de nivel primario no se repiten en los de nivel secundario.","        if i not in listanombresSecundaria:","            nombresnorepetidos.append(i)","nombresrepetidos=set(nombresrepetidos)","nombresnorepetidos=set(nombresnorepetidos)","print(nombresrepetidos)","print(nombresnorepetidos)","#7.\tEscribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:","#‘r’:5","#‘%’:3","#‘a’:8","#‘9’:1","","listastr=[]","contt=0","while True:","    string=input('ingrese una string: \\n')","    listastr.append(string)","    contt+=1","    if contt==50:","        break","listanuevastr=[]","tuplastr=()","for i in listastr:","    cont=0","    for k in listastr:","        if i ==k:","            cont+=1","            tuplastr=(i,cont)","    listanuevastr.append(tuplastr)   ","","listaset=set(listanuevastr)            ","print(listaset)","","#8 trabajo de los equipos de futbol","def res(matriz, num):","    contvic = 0","    contderr = 0","    contemp = 0","    conpuntos = 0","    for i in range(len(matriz)):","        for j in range(len(matriz)):","            if i != j:","                if i == num:","                    if matriz[i][j] \u003c matriz[j][i]:","                        contderr += 1","                    elif matriz[i][j] \u003e matriz[j][i]:","                        contvic += 1","                        conpuntos += 3","                    else:","                        conpuntos += 1","                        contemp += 1","    listaestadisticas = [contvic, contderr, contemp, conpuntos]","    return listaestadisticas","","","def dif(matriz, num):","    sum = 0","    golesrecibidos = 0","    cont = 0","    for i in matriz[num]:","        sum += i","        for i in range(len(matriz)):","            for j in range(len(matriz)):","                if i != j:","                    if cont == 3:","                        break","                    if i == num:","                        golesrecibidos += matriz[j][i]","","                        cont += 1","    res = sum - golesrecibidos","","    return f\"equipo{num+1} la diferencia es : {res} \"","","","matriz = [[0, 4, 2, 1], [5, 0, 3, 2], [0, 2, 0, 1], [1, 0, 2, 0]]","","estadisticasequipo1 = res(matriz, 0)","print(","    f\"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}, puntosTotales= {estadisticasequipo1[3]}\"",")","dif1 = dif(matriz, 0)","print(dif1)","","","estadisticasequipo2 = res(matriz, 1)","print(","    f\"Equipo 2: Victorias={estadisticasequipo2[0]}, Derrotas={estadisticasequipo2[1]}, Empates={estadisticasequipo2[2]},  puntosTotales= {estadisticasequipo2[3]}\"",")","dif2 = dif(matriz, 1)","print(dif2)","","estadisticasequipo3 = res(matriz, 2)","print(","    f\"Equipo 3: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}, puntosTotales= {estadisticasequipo3[3]}\"",")","dif3 = dif(matriz, 2)","print(dif3)","","estadisticasequipo4 = res(matriz, 3)","print(","    f\"Equipo 4: Victorias={estadisticasequipo4[0]}, Derrotas={estadisticasequipo4[1]}, Empates={estadisticasequipo4[2]}, puntosTotales= {estadisticasequipo4[3]}\"",")","dif4 = dif(matriz, 3)","print(dif4)"],"stylingDirectives":[[],[{"start":0,"end":156,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":64,"cssClass":"pl-s"},{"start":61,"end":63,"cssClass":"pl-cce"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-c1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-k"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":17,"cssClass":"pl-s1"}],[{"start":0,"end":179,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":16,"cssClass":"pl-en"},{"start":17,"end":56,"cssClass":"pl-s"},{"start":53,"end":55,"cssClass":"pl-cce"}],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":24,"cssClass":"pl-s1"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-en"},{"start":23,"end":29,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":17,"cssClass":"pl-s1"}],[{"start":0,"end":59,"cssClass":"pl-c"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":5,"end":6,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":10,"end":11,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":27,"cssClass":"pl-s"},{"start":20,"end":26,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-kos"},{"start":21,"end":25,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-kos"}],[{"start":0,"end":177,"cssClass":"pl-c"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-en"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":44,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-s1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":11,"cssClass":"pl-s1"}],[{"start":0,"end":284,"cssClass":"pl-c"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":25,"cssClass":"pl-s1"}],[{"start":4,"end":14,"cssClass":"pl-s1"},{"start":15,"end":21,"cssClass":"pl-en"},{"start":22,"end":27,"cssClass":"pl-s1"}],[],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-en"},{"start":13,"end":23,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":14,"cssClass":"pl-s1"}],[],[{"start":0,"end":249,"cssClass":"pl-c"}],[],[],[],[{"start":0,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":0,"end":22,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":77,"cssClass":"pl-s"},{"start":74,"end":76,"cssClass":"pl-cce"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":28,"cssClass":"pl-s1"},{"start":29,"end":35,"cssClass":"pl-en"},{"start":36,"end":44,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-k"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":79,"cssClass":"pl-s"},{"start":76,"end":78,"cssClass":"pl-cce"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-en"},{"start":38,"end":46,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-k"}],[{"start":0,"end":115,"cssClass":"pl-c"}],[{"start":0,"end":15,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":36,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":59,"cssClass":"pl-s1"}],[{"start":0,"end":17,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":18,"end":21,"cssClass":"pl-en"},{"start":22,"end":37,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":23,"cssClass":"pl-s1"}],[],[{"start":0,"end":85,"cssClass":"pl-c"}],[{"start":0,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":0,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":29,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":35,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-s1"}],[{"start":12,"end":28,"cssClass":"pl-s1"},{"start":29,"end":35,"cssClass":"pl-en"},{"start":36,"end":37,"cssClass":"pl-s1"}],[{"start":8,"end":92,"cssClass":"pl-c"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-c1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":42,"cssClass":"pl-s1"}],[{"start":12,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-en"},{"start":38,"end":39,"cssClass":"pl-s1"}],[{"start":0,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-en"},{"start":21,"end":37,"cssClass":"pl-s1"}],[{"start":0,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":41,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":22,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":24,"cssClass":"pl-s1"}],[{"start":0,"end":245,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-c"}],[],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":6,"end":7,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":11,"end":16,"cssClass":"pl-en"},{"start":17,"end":41,"cssClass":"pl-s"},{"start":38,"end":40,"cssClass":"pl-cce"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-en"},{"start":20,"end":26,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":9,"end":11,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-k"}],[{"start":0,"end":13,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":17,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-s1"},{"start":24,"end":28,"cssClass":"pl-s1"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":24,"cssClass":"pl-en"},{"start":25,"end":33,"cssClass":"pl-s1"}],[],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-en"},{"start":13,"end":26,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":14,"cssClass":"pl-s1"}],[],[{"start":0,"end":35,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-en"},{"start":8,"end":14,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-s1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-c1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":29,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-en"},{"start":27,"end":33,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-s1"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":23,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":38,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-s1"}],[{"start":24,"end":32,"cssClass":"pl-s1"},{"start":33,"end":35,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-c1"}],[{"start":20,"end":24,"cssClass":"pl-k"},{"start":25,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":40,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-s1"}],[{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":35,"end":36,"cssClass":"pl-c1"}],[{"start":24,"end":33,"cssClass":"pl-s1"},{"start":34,"end":36,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-c1"}],[{"start":20,"end":24,"cssClass":"pl-k"}],[{"start":24,"end":33,"cssClass":"pl-s1"},{"start":34,"end":36,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-c1"}],[{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":35,"end":36,"cssClass":"pl-c1"}],[{"start":4,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":25,"end":32,"cssClass":"pl-s1"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":44,"end":51,"cssClass":"pl-s1"},{"start":53,"end":62,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":28,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-en"},{"start":8,"end":14,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":11,"cssClass":"pl-c1"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-en"},{"start":27,"end":33,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-en"},{"start":31,"end":37,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-s1"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"}],[{"start":24,"end":29,"cssClass":"pl-k"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":23,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":31,"cssClass":"pl-s1"}],[{"start":24,"end":38,"cssClass":"pl-s1"},{"start":39,"end":41,"cssClass":"pl-c1"},{"start":42,"end":48,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-s1"}],[],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":33,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":30,"cssClass":"pl-s1"}],[],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":53,"cssClass":"pl-s"},{"start":19,"end":26,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-kos"},{"start":20,"end":23,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-kos"},{"start":46,"end":51,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-kos"},{"start":47,"end":50,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-kos"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":56,"end":57,"cssClass":"pl-c1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":62,"end":63,"cssClass":"pl-c1"}],[],[{"start":0,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":161,"cssClass":"pl-s"},{"start":26,"end":50,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-kos"},{"start":27,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-kos"},{"start":61,"end":85,"cssClass":"pl-s1"},{"start":61,"end":62,"cssClass":"pl-kos"},{"start":62,"end":81,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":84,"end":85,"cssClass":"pl-kos"},{"start":95,"end":119,"cssClass":"pl-s1"},{"start":95,"end":96,"cssClass":"pl-kos"},{"start":96,"end":115,"cssClass":"pl-s1"},{"start":116,"end":117,"cssClass":"pl-c1"},{"start":118,"end":119,"cssClass":"pl-kos"},{"start":136,"end":160,"cssClass":"pl-s1"},{"start":136,"end":137,"cssClass":"pl-kos"},{"start":137,"end":156,"cssClass":"pl-s1"},{"start":157,"end":158,"cssClass":"pl-c1"},{"start":159,"end":160,"cssClass":"pl-kos"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":162,"cssClass":"pl-s"},{"start":26,"end":50,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-kos"},{"start":27,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-kos"},{"start":61,"end":85,"cssClass":"pl-s1"},{"start":61,"end":62,"cssClass":"pl-kos"},{"start":62,"end":81,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":84,"end":85,"cssClass":"pl-kos"},{"start":95,"end":119,"cssClass":"pl-s1"},{"start":95,"end":96,"cssClass":"pl-kos"},{"start":96,"end":115,"cssClass":"pl-s1"},{"start":116,"end":117,"cssClass":"pl-c1"},{"start":118,"end":119,"cssClass":"pl-kos"},{"start":137,"end":161,"cssClass":"pl-s1"},{"start":137,"end":138,"cssClass":"pl-kos"},{"start":138,"end":157,"cssClass":"pl-s1"},{"start":158,"end":159,"cssClass":"pl-c1"},{"start":160,"end":161,"cssClass":"pl-kos"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":161,"cssClass":"pl-s"},{"start":26,"end":50,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-kos"},{"start":27,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-kos"},{"start":61,"end":85,"cssClass":"pl-s1"},{"start":61,"end":62,"cssClass":"pl-kos"},{"start":62,"end":81,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":84,"end":85,"cssClass":"pl-kos"},{"start":95,"end":119,"cssClass":"pl-s1"},{"start":95,"end":96,"cssClass":"pl-kos"},{"start":96,"end":115,"cssClass":"pl-s1"},{"start":116,"end":117,"cssClass":"pl-c1"},{"start":118,"end":119,"cssClass":"pl-kos"},{"start":136,"end":160,"cssClass":"pl-s1"},{"start":136,"end":137,"cssClass":"pl-kos"},{"start":137,"end":156,"cssClass":"pl-s1"},{"start":157,"end":158,"cssClass":"pl-c1"},{"start":159,"end":160,"cssClass":"pl-kos"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":161,"cssClass":"pl-s"},{"start":26,"end":50,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-kos"},{"start":27,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-kos"},{"start":61,"end":85,"cssClass":"pl-s1"},{"start":61,"end":62,"cssClass":"pl-kos"},{"start":62,"end":81,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":84,"end":85,"cssClass":"pl-kos"},{"start":95,"end":119,"cssClass":"pl-s1"},{"start":95,"end":96,"cssClass":"pl-kos"},{"start":96,"end":115,"cssClass":"pl-s1"},{"start":116,"end":117,"cssClass":"pl-c1"},{"start":118,"end":119,"cssClass":"pl-kos"},{"start":136,"end":160,"cssClass":"pl-s1"},{"start":136,"end":137,"cssClass":"pl-kos"},{"start":137,"end":156,"cssClass":"pl-s1"},{"start":157,"end":158,"cssClass":"pl-c1"},{"start":159,"end":160,"cssClass":"pl-kos"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/paulog16/Programacion1/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/paulog16/Programacion1/security/dependabot","repoSecurityAndAnalysisPath":"/paulog16/Programacion1/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"Trabajo_práctico_nro6.py","displayUrl":"https://github.com/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py?raw=true","headerInfo":{"blobSize":"5.98 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"d85c972","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fpaulog16%2FProgramacion1%2Fblob%2Fmain%2FTrabajo_pr%25C3%25A1ctico_nro6.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"180","truncatedSloc":"159"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/paulog16/Programacion1/discussions/new","newIssuePath":"/paulog16/Programacion1/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/paulog16/Programacion1/blob/main/Trabajo_pr%C3%A1ctico_nro6.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/paulog16/Programacion1/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/paulog16/Programacion1/raw/main/Trabajo_pr%C3%A1ctico_nro6.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"paulog16","repoName":"Programacion1","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"list_number","kind":"constant","ident_start":159,"ident_end":170,"extent_start":159,"extent_end":173,"fully_qualified_name":"list_number","ident_utf16":{"start":{"line_number":2,"utf16_col":0},"end":{"line_number":2,"utf16_col":11}},"extent_utf16":{"start":{"line_number":2,"utf16_col":0},"end":{"line_number":2,"utf16_col":14}}},{"name":"number","kind":"constant","ident_start":532,"ident_end":538,"extent_start":532,"extent_end":590,"fully_qualified_name":"number","ident_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":6}},"extent_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":58}}},{"name":"suma","kind":"constant","ident_start":784,"ident_end":788,"extent_start":784,"extent_end":790,"fully_qualified_name":"suma","ident_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":4}},"extent_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":6}}},{"name":"other_number","kind":"constant","ident_start":1038,"ident_end":1050,"extent_start":1038,"extent_end":1084,"fully_qualified_name":"other_number","ident_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":12}},"extent_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":46}}},{"name":"other_lista","kind":"constant","ident_start":1085,"ident_end":1096,"extent_start":1085,"extent_end":1099,"fully_qualified_name":"other_lista","ident_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":11}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":14}}},{"name":"listanueva","kind":"constant","ident_start":1497,"ident_end":1507,"extent_start":1497,"extent_end":1510,"fully_qualified_name":"listanueva","ident_utf16":{"start":{"line_number":31,"utf16_col":0},"end":{"line_number":31,"utf16_col":10}},"extent_utf16":{"start":{"line_number":31,"utf16_col":0},"end":{"line_number":31,"utf16_col":13}}},{"name":"tupla","kind":"constant","ident_start":1511,"ident_end":1516,"extent_start":1511,"extent_end":1519,"fully_qualified_name":"tupla","ident_utf16":{"start":{"line_number":32,"utf16_col":0},"end":{"line_number":32,"utf16_col":5}},"extent_utf16":{"start":{"line_number":32,"utf16_col":0},"end":{"line_number":32,"utf16_col":8}}},{"name":"listaset","kind":"constant","ident_start":1677,"ident_end":1685,"extent_start":1677,"extent_end":1701,"fully_qualified_name":"listaset","ident_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":8}},"extent_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":24}}},{"name":"listanombresPrimaria","kind":"constant","ident_start":1997,"ident_end":2017,"extent_start":1997,"extent_end":2020,"fully_qualified_name":"listanombresPrimaria","ident_utf16":{"start":{"line_number":48,"utf16_col":0},"end":{"line_number":48,"utf16_col":20}},"extent_utf16":{"start":{"line_number":48,"utf16_col":0},"end":{"line_number":48,"utf16_col":23}}},{"name":"listanombresSecundaria","kind":"constant","ident_start":2021,"ident_end":2043,"extent_start":2021,"extent_end":2046,"fully_qualified_name":"listanombresSecundaria","ident_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":49,"utf16_col":22}},"extent_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":49,"utf16_col":25}}},{"name":"todoslosnombres","kind":"constant","ident_start":2557,"ident_end":2572,"extent_start":2557,"extent_end":2616,"fully_qualified_name":"todoslosnombres","ident_utf16":{"start":{"line_number":63,"utf16_col":0},"end":{"line_number":63,"utf16_col":15}},"extent_utf16":{"start":{"line_number":63,"utf16_col":0},"end":{"line_number":63,"utf16_col":59}}},{"name":"nombressinrepetir","kind":"constant","ident_start":2617,"ident_end":2634,"extent_start":2617,"extent_end":2655,"fully_qualified_name":"nombressinrepetir","ident_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":17}},"extent_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":38}}},{"name":"nombresrepetidos","kind":"constant","ident_start":2769,"ident_end":2785,"extent_start":2769,"extent_end":2788,"fully_qualified_name":"nombresrepetidos","ident_utf16":{"start":{"line_number":68,"utf16_col":0},"end":{"line_number":68,"utf16_col":16}},"extent_utf16":{"start":{"line_number":68,"utf16_col":0},"end":{"line_number":68,"utf16_col":19}}},{"name":"nombresnorepetidos","kind":"constant","ident_start":2789,"ident_end":2807,"extent_start":2789,"extent_end":2810,"fully_qualified_name":"nombresnorepetidos","ident_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":18}},"extent_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":21}}},{"name":"nombresrepetidos","kind":"constant","ident_start":3114,"ident_end":3130,"extent_start":3114,"extent_end":3152,"fully_qualified_name":"nombresrepetidos","ident_utf16":{"start":{"line_number":77,"utf16_col":0},"end":{"line_number":77,"utf16_col":16}},"extent_utf16":{"start":{"line_number":77,"utf16_col":0},"end":{"line_number":77,"utf16_col":38}}},{"name":"nombresnorepetidos","kind":"constant","ident_start":3153,"ident_end":3171,"extent_start":3153,"extent_end":3195,"fully_qualified_name":"nombresnorepetidos","ident_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":78,"utf16_col":18}},"extent_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":78,"utf16_col":42}}},{"name":"listastr","kind":"constant","ident_start":3538,"ident_end":3546,"extent_start":3538,"extent_end":3549,"fully_qualified_name":"listastr","ident_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":8}},"extent_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":11}}},{"name":"contt","kind":"constant","ident_start":3550,"ident_end":3555,"extent_start":3550,"extent_end":3557,"fully_qualified_name":"contt","ident_utf16":{"start":{"line_number":88,"utf16_col":0},"end":{"line_number":88,"utf16_col":5}},"extent_utf16":{"start":{"line_number":88,"utf16_col":0},"end":{"line_number":88,"utf16_col":7}}},{"name":"listanuevastr","kind":"constant","ident_start":3686,"ident_end":3699,"extent_start":3686,"extent_end":3702,"fully_qualified_name":"listanuevastr","ident_utf16":{"start":{"line_number":95,"utf16_col":0},"end":{"line_number":95,"utf16_col":13}},"extent_utf16":{"start":{"line_number":95,"utf16_col":0},"end":{"line_number":95,"utf16_col":16}}},{"name":"tuplastr","kind":"constant","ident_start":3703,"ident_end":3711,"extent_start":3703,"extent_end":3714,"fully_qualified_name":"tuplastr","ident_utf16":{"start":{"line_number":96,"utf16_col":0},"end":{"line_number":96,"utf16_col":8}},"extent_utf16":{"start":{"line_number":96,"utf16_col":0},"end":{"line_number":96,"utf16_col":11}}},{"name":"listaset","kind":"constant","ident_start":3875,"ident_end":3883,"extent_start":3875,"extent_end":3902,"fully_qualified_name":"listaset","ident_utf16":{"start":{"line_number":105,"utf16_col":0},"end":{"line_number":105,"utf16_col":8}},"extent_utf16":{"start":{"line_number":105,"utf16_col":0},"end":{"line_number":105,"utf16_col":27}}},{"name":"res","kind":"function","ident_start":3972,"ident_end":3975,"extent_start":3968,"extent_end":4593,"fully_qualified_name":"res","ident_utf16":{"start":{"line_number":109,"utf16_col":4},"end":{"line_number":109,"utf16_col":7}},"extent_utf16":{"start":{"line_number":109,"utf16_col":0},"end":{"line_number":127,"utf16_col":28}}},{"name":"dif","kind":"function","ident_start":4600,"ident_end":4603,"extent_start":4596,"extent_end":5086,"fully_qualified_name":"dif","ident_utf16":{"start":{"line_number":130,"utf16_col":4},"end":{"line_number":130,"utf16_col":7}},"extent_utf16":{"start":{"line_number":130,"utf16_col":0},"end":{"line_number":147,"utf16_col":53}}},{"name":"matriz","kind":"constant","ident_start":5089,"ident_end":5095,"extent_start":5089,"extent_end":5154,"fully_qualified_name":"matriz","ident_utf16":{"start":{"line_number":150,"utf16_col":0},"end":{"line_number":150,"utf16_col":6}},"extent_utf16":{"start":{"line_number":150,"utf16_col":0},"end":{"line_number":150,"utf16_col":65}}},{"name":"estadisticasequipo1","kind":"constant","ident_start":5156,"ident_end":5175,"extent_start":5156,"extent_end":5192,"fully_qualified_name":"estadisticasequipo1","ident_utf16":{"start":{"line_number":152,"utf16_col":0},"end":{"line_number":152,"utf16_col":19}},"extent_utf16":{"start":{"line_number":152,"utf16_col":0},"end":{"line_number":152,"utf16_col":36}}},{"name":"dif1","kind":"constant","ident_start":5364,"ident_end":5368,"extent_start":5364,"extent_end":5385,"fully_qualified_name":"dif1","ident_utf16":{"start":{"line_number":156,"utf16_col":0},"end":{"line_number":156,"utf16_col":4}},"extent_utf16":{"start":{"line_number":156,"utf16_col":0},"end":{"line_number":156,"utf16_col":21}}},{"name":"estadisticasequipo2","kind":"constant","ident_start":5400,"ident_end":5419,"extent_start":5400,"extent_end":5436,"fully_qualified_name":"estadisticasequipo2","ident_utf16":{"start":{"line_number":160,"utf16_col":0},"end":{"line_number":160,"utf16_col":19}},"extent_utf16":{"start":{"line_number":160,"utf16_col":0},"end":{"line_number":160,"utf16_col":36}}},{"name":"dif2","kind":"constant","ident_start":5609,"ident_end":5613,"extent_start":5609,"extent_end":5630,"fully_qualified_name":"dif2","ident_utf16":{"start":{"line_number":164,"utf16_col":0},"end":{"line_number":164,"utf16_col":4}},"extent_utf16":{"start":{"line_number":164,"utf16_col":0},"end":{"line_number":164,"utf16_col":21}}},{"name":"estadisticasequipo3","kind":"constant","ident_start":5644,"ident_end":5663,"extent_start":5644,"extent_end":5680,"fully_qualified_name":"estadisticasequipo3","ident_utf16":{"start":{"line_number":167,"utf16_col":0},"end":{"line_number":167,"utf16_col":19}},"extent_utf16":{"start":{"line_number":167,"utf16_col":0},"end":{"line_number":167,"utf16_col":36}}},{"name":"dif3","kind":"constant","ident_start":5852,"ident_end":5856,"extent_start":5852,"extent_end":5873,"fully_qualified_name":"dif3","ident_utf16":{"start":{"line_number":171,"utf16_col":0},"end":{"line_number":171,"utf16_col":4}},"extent_utf16":{"start":{"line_number":171,"utf16_col":0},"end":{"line_number":171,"utf16_col":21}}},{"name":"estadisticasequipo4","kind":"constant","ident_start":5887,"ident_end":5906,"extent_start":5887,"extent_end":5923,"fully_qualified_name":"estadisticasequipo4","ident_utf16":{"start":{"line_number":174,"utf16_col":0},"end":{"line_number":174,"utf16_col":19}},"extent_utf16":{"start":{"line_number":174,"utf16_col":0},"end":{"line_number":174,"utf16_col":36}}},{"name":"dif4","kind":"constant","ident_start":6095,"ident_end":6099,"extent_start":6095,"extent_end":6116,"fully_qualified_name":"dif4","ident_utf16":{"start":{"line_number":178,"utf16_col":0},"end":{"line_number":178,"utf16_col":4}},"extent_utf16":{"start":{"line_number":178,"utf16_col":0},"end":{"line_number":178,"utf16_col":21}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"csrf_tokens":{"/paulog16/Programacion1/branches":{"post":"nLztajD_g4xFMjs7cBtrQQWXCS46utZT1qe5joAzTghSdRWA_CGg_21lHwciStF0M-MS4K6qzMB1hZtbMKpBGg"},"/repos/preferences":{"post":"bHlcT-2r5NHJtwz7ahU8Iu8_oOsF2PK8pUDLw446fxUMMeasBOuRKg28X25dZV0_TRVmUCePSY8nZACcfB_XWg"}}},"title":"Programacion1/Trabajo_práctico_nro6.py at main · paulog16/Programacion1","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-83d4418b406d.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-bcc43f789400.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_streaming":false,"copilot_popover_file_editor_header":true,"copilot_smell_icebreaker_ux":false}}}</script>
  <div data-target="react-app.reactRoot"><style data-styled="true" data-styled-version="5.3.6">.fNPcqd{font-weight:600;font-size:32px;margin:0;font-size:14px;}/*!sc*/
.imcwCi{font-weight:600;font-size:32px;margin:0;font-size:16px;margin-left:8px;}/*!sc*/
.cgQnMS{font-weight:600;font-size:32px;margin:0;}/*!sc*/
.diwsLq{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:16px;}/*!sc*/
.jAEDJk{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:14px;}/*!sc*/
data-styled.g1[id="Heading__StyledHeading-sc-1c1dgg0-0"]{content:"fNPcqd,imcwCi,cgQnMS,diwsLq,jAEDJk,"}/*!sc*/
.fSWWem{padding:0;}/*!sc*/
.kPPmzM{max-width:100%;margin-left:auto;margin-right:auto;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;}/*!sc*/
.cIAPDV{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;}/*!sc*/
.gvCnwW{width:100%;}/*!sc*/
@media screen and (min-width:544px){.gvCnwW{width:100%;}}/*!sc*/
@media screen and (min-width:768px){.gvCnwW{width:auto;}}/*!sc*/
.kFEKvZ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-order:1;-ms-flex-order:1;order:1;width:100%;margin-left:0;margin-right:0;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin-bottom:0;min-width:0;}/*!sc*/
@media screen and (min-width:544px){.kFEKvZ{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}}/*!sc*/
@media screen and (min-width:768px){.kFEKvZ{width:auto;margin-top:0 !important;margin-bottom:0 !important;position:-webkit-sticky;position:sticky;top:0px;max-height:var(--sticky-pane-height);-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse;margin-right:0;}}/*!sc*/
@media screen and (min-width:769px){.kFEKvZ{height:100vh;max-height:100vh !important;}}/*!sc*/
@media print,screen and (max-width:1349px) and (min-width:768px){.kFEKvZ{display:none;}}/*!sc*/
.eUyHuk{margin-left:0;margin-right:0;display:none;margin-top:0;}/*!sc*/
@media screen and (min-width:768px){.eUyHuk{margin-left:0 !important;margin-right:0 !important;}}/*!sc*/
.hAeDYA{height:100%;position:relative;display:none;margin-left:0;}/*!sc*/
.ekKrwo{position:absolute;inset:0 -2px;cursor:col-resize;background-color:transparent;-webkit-transition-delay:0.1s;transition-delay:0.1s;}/*!sc*/
.ekKrwo:hover{background-color:rgba(175,184,193,0.2);}/*!sc*/
.gNdDUH{--pane-min-width:256px;--pane-max-width-diff:511px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));width:100%;padding:0;}/*!sc*/
@media screen and (min-width:544px){}/*!sc*/
@media screen and (min-width:768px){.gNdDUH{width:clamp(var(--pane-min-width),var(--pane-width),var(--pane-max-width));overflow:auto;}}/*!sc*/
@media screen and (min-width:1280px){.gNdDUH{--pane-max-width-diff:959px;}}/*!sc*/
.jywUSN{max-height:100%;height:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
@media screen and (max-width:768px){.jywUSN{display:none;}}/*!sc*/
@media screen and (min-width:768px){.jywUSN{max-height:100vh;height:100vh;}}/*!sc*/
.hBSSUC{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-left:16px;padding-right:16px;padding-bottom:8px;padding-top:16px;}/*!sc*/
.iPurHz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-bottom:16px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kkrdEu{-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}/*!sc*/
.trpoQ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;pointer-events:none;}/*!sc*/
.hVHHYa{margin-left:24px;margin-right:24px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.idZfsJ{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;}/*!sc*/
.bKgizp{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.kYlvBX{margin-right:4px;color:#656d76;}/*!sc*/
.caeYDk{font-size:14px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.jahcnb{margin-left:8px;white-space:nowrap;}/*!sc*/
.jahcnb:hover button:not(:hover){border-left-color:var(--button-default-borderColor-hover,var(--color-btn-hover-border));}/*!sc*/
.ccToMy{margin-left:16px;margin-right:16px;margin-bottom:12px;}/*!sc*/
@media screen and (max-width:768px){.ccToMy{display:none;}}/*!sc*/
.cNvKlH{margin-right:-6px;}/*!sc*/
.cLfAnm{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;max-height:100% !important;overflow-y:auto;-webkit-scrollbar-gutter:stable;-moz-scrollbar-gutter:stable;-ms-scrollbar-gutter:stable;scrollbar-gutter:stable;}/*!sc*/
@media screen and (max-width:768px){.cLfAnm{display:none;}}/*!sc*/
.erWCJP{padding-left:16px;padding-right:16px;padding-bottom:8px;}/*!sc*/
@media (min-height:600px) and (min-width:768px){.hwhShM{display:none;}}/*!sc*/
.cYPxpP{margin-top:8px;margin-left:16px;margin-right:16px;margin-bottom:12px;font-size:12px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
@media (max-height:599px),(max-width:767px){.fBtiVT{display:none;}}/*!sc*/
.emFMJu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-order:2;-ms-flex-order:2;order:2;-webkit-flex-basis:0;-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;min-width:1px;margin-right:auto;}/*!sc*/
@media print{.emFMJu{display:-webkit-box !important;display:-webkit-flex !important;display:-ms-flexbox !important;display:flex !important;}}/*!sc*/
.hlUAHL{width:100%;max-width:100%;margin-left:auto;margin-right:auto;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;padding:0;}/*!sc*/
.iStsmI{margin-left:auto;margin-right:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:40px;max-width:100%;margin-top:0;}/*!sc*/
.eIgvIk{display:inherit;}/*!sc*/
.eVFfWF{width:100%;}/*!sc*/
.kgXdnT{padding:16px;padding-bottom:0;}/*!sc*/
.kzTa-dF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:16px;width:100%;}/*!sc*/
.bbXCl{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;}/*!sc*/
.hGGMNu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;justify-self:flex-end;}/*!sc*/
.eHRrYV{margin-left:8px;margin-right:8px;}/*!sc*/
.dKmYfk{font-size:14px;min-width:0;max-width:125px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.hSNzKh{justify-self:end;max-width:100%;}/*!sc*/
.eTvGbF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:16px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kzRgrI{max-width:100%;}/*!sc*/
.cmAPIB{max-width:100%;list-style:none;display:inline-block;}/*!sc*/
.jwXCBK{display:inline-block;max-width:100%;}/*!sc*/
.bDwCYs{padding:16px;padding-bottom:0;padding-left:16px;padding-right:16px;}/*!sc*/
.fywjmm{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;}/*!sc*/
.dyczTK{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:8px;}/*!sc*/
.kszRgZ{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;padding-right:8px;min-width:0;}/*!sc*/
.gtBUEp{min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;}/*!sc*/
.MERGN{margin-left:16px;margin-right:16px;}/*!sc*/
@media screen and (min-width:1440px){.MERGN{margin-left:16px;}}/*!sc*/
.cMYnca{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
.kLxXov{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;border:1px solid;border-color:#d0d7de;border-radius:6px;margin-bottom:16px;}/*!sc*/
.eYedVD{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:273px;padding-right:8px;padding-left:16px;padding-top:8px;padding-bottom:8px;}/*!sc*/
.jGfYmh{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;}/*!sc*/
.lhFvfi{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bqgLjk{display:inherit;}/*!sc*/
@media screen and (min-width:544px){.bqgLjk{display:none;}}/*!sc*/
@media screen and (min-width:768px){.bqgLjk{display:none;}}/*!sc*/
.iJmJly{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}/*!sc*/
.kjydbF{width:100%;height:-webkit-fit-content;height:-moz-fit-content;height:fit-content;min-width:0;margin-right:16px;}/*!sc*/
.bSdwWB{padding-left:4px;padding-bottom:16px;}/*!sc*/
.fleZSW{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bZpGqz{font-size:12px;-webkit-flex:auto;-ms-flex:auto;flex:auto;padding-right:16px;color:#656d76;min-width:0;}/*!sc*/
.gBKNLX{top:0px;z-index:1;background:var(--color-canvas-default);position:-webkit-sticky;position:sticky;}/*!sc*/
.ePiodO{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;position:absolute;}/*!sc*/
.kQJlnf{display:none;min-width:0;padding-top:8px;padding-bottom:8px;}/*!sc*/
.gJICKO{margin-right:8px;margin-left:16px;text-overflow:ellipsis;overflow:hidden;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;width:100%;}/*!sc*/
.iZJewz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:14px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bvEDG{padding-left:8px;padding-top:8px;padding-bottom:8px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;background-color:#f6f8fa;border:1px solid var(--borderColor-default,var(--color-border-default));border-radius:6px 6px 0px 0px;}/*!sc*/
.bfkNRF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:0;}/*!sc*/
.fXBLEV{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:transparent;}/*!sc*/
.fXBLEV:not(:last-child){margin-right:1px;}/*!sc*/
.fXBLEV:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.fXBLEV:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.fXBLEV:first-child{margin-left:-1px;}/*!sc*/
.fXBLEV:last-child{margin-right:-1px;}/*!sc*/
.jkTWSe{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:#d0d7de;}/*!sc*/
.jkTWSe:not(:last-child){margin-right:1px;}/*!sc*/
.jkTWSe:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.jkTWSe:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.jkTWSe:first-child{margin-left:-1px;}/*!sc*/
.jkTWSe:last-child{margin-right:-1px;}/*!sc*/
.iBylDf{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;margin-right:8px;}/*!sc*/
.kSGBPx{gap:8px;}/*!sc*/
.flDsrw{border:1px solid;border-top:none;border-color:#d0d7de;border-radius:0px 0px 6px 6px;min-width:273px;}/*!sc*/
.jWnGGx{background-color:var(--bgColor-default,var(--color-canvas-default));border:0px;border-width:0;border-radius:0px 0px 6px 6px;padding:0;min-width:0;margin-top:46px;}/*!sc*/
.TCenl{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;padding-top:8px;padding-bottom:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;min-width:0;position:relative;}/*!sc*/
.cluMzC{position:relative;}/*!sc*/
.eRkHwF{-webkit-flex:1;-ms-flex:1;flex:1;position:relative;min-width:0;}/*!sc*/
.knCTAx{tab-size:8;isolation:isolate;position:relative;overflow:auto;max-width:unset;}/*!sc*/
.hXUKEK{margin:1px 8px;position:absolute;z-index:1;}/*!sc*/
.cXzIIR{position:absolute;}/*!sc*/
.ktQnIo{padding-bottom:33px;}/*!sc*/
.bgHcBP{background-color:#ffffff;border:1px solid;border-color:#d0d7de;border-radius:6px;contain:paint;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;height:100%;min-height:0;max-height:100vh;overflow-y:auto;right:0;top:0px;z-index:1;background:var(--color-canvas-default);position:-webkit-sticky;position:sticky;}/*!sc*/
.bJNAmt{padding-top:8px;padding-bottom:8px;padding-left:16px;padding-right:16px;}/*!sc*/
.ipXucK{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;}/*!sc*/
.wMEyi{font-size:14px;-webkit-order:1;-ms-flex-order:1;order:1;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-weight:600;}/*!sc*/
.igdeeu{font-size:12px;color:#656d76;padding-top:8px;}/*!sc*/
.ckwgci{margin-right:6px;}/*!sc*/
.jGYebd{margin-left:-16px;margin-bottom:-8px;}/*!sc*/
.kgNotW{margin-bottom:-8px;overflow-y:auto;max-height:calc(100vh - 237px);padding-left:16px;padding-bottom:8px;padding-top:4px;}/*!sc*/
.cFPoqW{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}/*!sc*/
.brdoto{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;position:relative;margin-right:8px;}/*!sc*/
.fQgtqx{background-color:#953800;opacity:0.1;position:absolute;border-radius:5px;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;height:100%;}/*!sc*/
.EVPPH{color:#953800;border-radius:5px;font-weight:600;font-size:smaller;padding-left:4px;padding-right:4px;padding-top:1px;padding-bottom:1px;}/*!sc*/
.gJbnxT{background-color:#6639ba;opacity:0.1;position:absolute;border-radius:5px;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;height:100%;}/*!sc*/
.cwQfpp{color:#6639ba;border-radius:5px;font-weight:600;font-size:smaller;padding-left:4px;padding-right:4px;padding-top:1px;padding-bottom:1px;}/*!sc*/
.aZrVR{position:fixed;top:0;right:0;height:100%;width:15px;-webkit-transition:-webkit-transform 0.3s;-webkit-transition:transform 0.3s;transition:transform 0.3s;z-index:1;}/*!sc*/
.aZrVR:hover{-webkit-transform:scaleX(1.5);-ms-transform:scaleX(1.5);transform:scaleX(1.5);}/*!sc*/
data-styled.g2[id="Box-sc-g0xbh4-0"]{content:"fSWWem,kPPmzM,cIAPDV,gvCnwW,kFEKvZ,eUyHuk,hAeDYA,ekKrwo,gNdDUH,jywUSN,hBSSUC,iPurHz,kkrdEu,trpoQ,hVHHYa,idZfsJ,bKgizp,kYlvBX,caeYDk,jahcnb,ccToMy,cNvKlH,cLfAnm,erWCJP,hwhShM,cYPxpP,fBtiVT,emFMJu,hlUAHL,iStsmI,eIgvIk,eVFfWF,kgXdnT,kzTa-dF,bbXCl,hGGMNu,eHRrYV,dKmYfk,hSNzKh,eTvGbF,kzRgrI,cmAPIB,jwXCBK,bDwCYs,fywjmm,dyczTK,kszRgZ,gtBUEp,MERGN,cMYnca,kLxXov,eYedVD,jGfYmh,lhFvfi,bqgLjk,iJmJly,kjydbF,bSdwWB,fleZSW,bZpGqz,gBKNLX,ePiodO,kQJlnf,gJICKO,iZJewz,bvEDG,bfkNRF,fXBLEV,jkTWSe,iBylDf,kSGBPx,flDsrw,jWnGGx,TCenl,cluMzC,eRkHwF,knCTAx,hXUKEK,cXzIIR,ktQnIo,bgHcBP,bJNAmt,ipXucK,wMEyi,igdeeu,ckwgci,jGYebd,kgNotW,cFPoqW,brdoto,fQgtqx,EVPPH,gJbnxT,cwQfpp,aZrVR,"}/*!sc*/
.rTZSs{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g3[id="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0"]{content:"rTZSs,"}/*!sc*/
.fUpWeN{display:inline-block;overflow:hidden;text-overflow:ellipsis;vertical-align:top;white-space:nowrap;max-width:125px;max-width:100%;}/*!sc*/
.iQHhGT{display:inherit;overflow:hidden;text-overflow:ellipsis;vertical-align:initial;white-space:nowrap;max-width:125px;max-width:180px;display:block;}/*!sc*/
data-styled.g5[id="Truncate__StyledTruncate-sc-23o1d2-0"]{content:"fUpWeN,iQHhGT,"}/*!sc*/
.fIqerb{color:#0969da;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fIqerb:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.fIqerb:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
.eVjWum{color:#0969da;-webkit-text-decoration:none;text-decoration:none;font-weight:600;}/*!sc*/
.eVjWum:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.eVjWum:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
data-styled.g7[id="Link__StyledLink-sc-14289xe-0"]{content:"fIqerb,eVjWum,"}/*!sc*/
.cgNHBf{font-size:14px;line-height:20px;color:#1F2328;vertical-align:middle;background-color:#ffffff;border:1px solid var(--control-borderColor-rest,#d0d7de);border-radius:6px;outline:none;box-shadow:inset 0 1px 0 rgba(208,215,222,0.2);display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.cgNHBf input,.cgNHBf textarea{cursor:text;}/*!sc*/
.cgNHBf select{cursor:pointer;}/*!sc*/
.cgNHBf::-webkit-input-placeholder{color:#6e7781;}/*!sc*/
.cgNHBf::-moz-placeholder{color:#6e7781;}/*!sc*/
.cgNHBf:-ms-input-placeholder{color:#6e7781;}/*!sc*/
.cgNHBf::placeholder{color:#6e7781;}/*!sc*/
.cgNHBf:focus-within{border-color:#0969da;outline:none;box-shadow:inset 0 0 0 1px #0969da;}/*!sc*/
.cgNHBf > textarea{padding:12px;}/*!sc*/
@media (min-width:768px){.cgNHBf{font-size:14px;}}/*!sc*/
.hdWBGU{font-size:14px;line-height:20px;color:#1F2328;vertical-align:middle;background-color:#ffffff;border:1px solid var(--control-borderColor-rest,#d0d7de);border-radius:6px;outline:none;box-shadow:inset 0 1px 0 rgba(208,215,222,0.2);display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;min-height:32px;width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-self:stretch;-ms-flex-item-align:stretch;align-self:stretch;margin-top:8px;border-radius:6px;}/*!sc*/
.hdWBGU input,.hdWBGU textarea{cursor:text;}/*!sc*/
.hdWBGU select{cursor:pointer;}/*!sc*/
.hdWBGU::-webkit-input-placeholder{color:#6e7781;}/*!sc*/
.hdWBGU::-moz-placeholder{color:#6e7781;}/*!sc*/
.hdWBGU:-ms-input-placeholder{color:#6e7781;}/*!sc*/
.hdWBGU::placeholder{color:#6e7781;}/*!sc*/
.hdWBGU > textarea{padding:12px;}/*!sc*/
@media (min-width:768px){.hdWBGU{font-size:14px;}}/*!sc*/
data-styled.g25[id="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0"]{content:"cgNHBf,hdWBGU,"}/*!sc*/
.cuQjCh{background-repeat:no-repeat;background-position:right 8px center;padding-left:12px;padding-right:12px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.cuQjCh > :not(:last-child){margin-right:8px;}/*!sc*/
.cuQjCh .TextInput-icon,.cuQjCh .TextInput-action{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;color:#656d76;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;}/*!sc*/
.cuQjCh > input,.cuQjCh > select{padding-left:0;padding-right:0;}/*!sc*/
.kdlhpP{background-repeat:no-repeat;background-position:right 8px center;padding-left:12px;padding-right:0;margin-top:8px;border-radius:6px;}/*!sc*/
.kdlhpP > :not(:last-child){margin-right:8px;}/*!sc*/
.kdlhpP .TextInput-icon,.kdlhpP .TextInput-action{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;color:#656d76;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;}/*!sc*/
.kdlhpP > input,.kdlhpP > select{padding-left:0;padding-right:0;}/*!sc*/
data-styled.g26[id="TextInputWrapper-sc-1mqhpbi-1"]{content:"cuQjCh,kdlhpP,"}/*!sc*/
.iBwhhC{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.iBwhhC:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iBwhhC:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iBwhhC:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iBwhhC[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iBwhhC[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iBwhhC:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iBwhhC:active{-webkit-transition:none;transition:none;}/*!sc*/
.iBwhhC:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.iBwhhC:disabled [data-component=ButtonCounter],.iBwhhC:disabled [data-component="leadingVisual"],.iBwhhC:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iBwhhC:focus{outline:solid 1px transparent;}}/*!sc*/
.iBwhhC [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iBwhhC[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iBwhhC[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iBwhhC[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iBwhhC[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iBwhhC[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iBwhhC[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iBwhhC[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iBwhhC[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iBwhhC[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iBwhhC[data-block="block"]{width:100%;}/*!sc*/
.iBwhhC [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.iBwhhC [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iBwhhC [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iBwhhC [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.iBwhhC [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iBwhhC [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iBwhhC:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.iBwhhC:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.iBwhhC[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.iBwhhC[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.iBwhhC[data-no-visuals]{color:#0969da;}/*!sc*/
.iBwhhC:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.iBwhhC:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.iBwhhC:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.iBwhhC{color:#656d76;padding-left:8px;padding-right:8px;display:none;}/*!sc*/
@media screen and (max-width:768px){.iBwhhC{display:block;}}/*!sc*/
.bpzCPD{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.bpzCPD:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.bpzCPD:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bpzCPD:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.bpzCPD[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bpzCPD[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bpzCPD:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bpzCPD:active{-webkit-transition:none;transition:none;}/*!sc*/
.bpzCPD:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.bpzCPD:disabled [data-component=ButtonCounter],.bpzCPD:disabled [data-component="leadingVisual"],.bpzCPD:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bpzCPD:focus{outline:solid 1px transparent;}}/*!sc*/
.bpzCPD [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bpzCPD[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bpzCPD[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bpzCPD[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bpzCPD[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bpzCPD[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bpzCPD[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bpzCPD[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bpzCPD[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bpzCPD[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bpzCPD[data-block="block"]{width:100%;}/*!sc*/
.bpzCPD [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.bpzCPD [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bpzCPD [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bpzCPD [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.bpzCPD [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bpzCPD [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bpzCPD:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.bpzCPD:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.bpzCPD[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.bpzCPD[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.bpzCPD[data-no-visuals]{color:#0969da;}/*!sc*/
.bpzCPD:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.bpzCPD:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.bpzCPD:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.bpzCPD[data-no-visuals="true"]{color:#656d76;height:32px;position:relative;}/*!sc*/
@media screen and (max-width:768px){.bpzCPD[data-no-visuals="true"]{display:none;}}/*!sc*/
.cpGorR{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.cpGorR:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.cpGorR:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.cpGorR:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.cpGorR[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.cpGorR[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cpGorR:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.cpGorR:active{-webkit-transition:none;transition:none;}/*!sc*/
.cpGorR:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.cpGorR:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.cpGorR:focus{outline:solid 1px transparent;}}/*!sc*/
.cpGorR [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cpGorR[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.cpGorR[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.cpGorR[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.cpGorR[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cpGorR[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.cpGorR[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.cpGorR[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.cpGorR[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cpGorR[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.cpGorR[data-block="block"]{width:100%;}/*!sc*/
.cpGorR [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.cpGorR [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.cpGorR [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.cpGorR [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.cpGorR [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.cpGorR [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cpGorR:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.cpGorR:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.cpGorR[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.cpGorR [data-component="leadingVisual"],.cpGorR [data-component="trailingVisual"],.cpGorR [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.cpGorR{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:0;}/*!sc*/
.cpGorR svg{color:#656d76;}/*!sc*/
.cpGorR > span{width:inherit;}/*!sc*/
.jOqXES{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.jOqXES:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.jOqXES:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jOqXES:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.jOqXES[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jOqXES[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jOqXES:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jOqXES:active{-webkit-transition:none;transition:none;}/*!sc*/
.jOqXES:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.jOqXES:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jOqXES:focus{outline:solid 1px transparent;}}/*!sc*/
.jOqXES [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jOqXES[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jOqXES[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jOqXES[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jOqXES[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jOqXES[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jOqXES[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jOqXES[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jOqXES[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jOqXES[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jOqXES[data-block="block"]{width:100%;}/*!sc*/
.jOqXES [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.jOqXES [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jOqXES [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jOqXES [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.jOqXES [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jOqXES [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jOqXES:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.jOqXES:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.jOqXES[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.jOqXES [data-component="leadingVisual"],.jOqXES [data-component="trailingVisual"],.jOqXES [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.jOqXES[data-no-visuals="true"]{color:#6e7781;border-top-right-radius:0;border-bottom-right-radius:0;border-right:0;}/*!sc*/
.dQkDZk{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.dQkDZk:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.dQkDZk:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.dQkDZk:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.dQkDZk[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.dQkDZk[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dQkDZk:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.dQkDZk:active{-webkit-transition:none;transition:none;}/*!sc*/
.dQkDZk:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.dQkDZk:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.dQkDZk:focus{outline:solid 1px transparent;}}/*!sc*/
.dQkDZk [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dQkDZk[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.dQkDZk[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.dQkDZk[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.dQkDZk[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dQkDZk[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.dQkDZk[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.dQkDZk[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.dQkDZk[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dQkDZk[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.dQkDZk[data-block="block"]{width:100%;}/*!sc*/
.dQkDZk [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.dQkDZk [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.dQkDZk [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.dQkDZk [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.dQkDZk [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.dQkDZk [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dQkDZk:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.dQkDZk:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.dQkDZk[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.dQkDZk [data-component="leadingVisual"],.dQkDZk [data-component="trailingVisual"],.dQkDZk [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.dQkDZk[data-no-visuals="true"]{color:#6e7781;font-size:14px;font-weight:400;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.iwngiV{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.iwngiV:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iwngiV:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iwngiV:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iwngiV[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iwngiV[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iwngiV:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iwngiV:active{-webkit-transition:none;transition:none;}/*!sc*/
.iwngiV:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.iwngiV:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iwngiV:focus{outline:solid 1px transparent;}}/*!sc*/
.iwngiV [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iwngiV[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iwngiV[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iwngiV[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iwngiV[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iwngiV[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iwngiV[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iwngiV[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iwngiV[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iwngiV[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iwngiV[data-block="block"]{width:100%;}/*!sc*/
.iwngiV [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.iwngiV [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iwngiV [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iwngiV [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.iwngiV [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iwngiV [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iwngiV:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.iwngiV:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.iwngiV[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.iwngiV [data-component="leadingVisual"],.iwngiV [data-component="trailingVisual"],.iwngiV [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.iwngiV{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}/*!sc*/
.iwngiV svg{color:#656d76;}/*!sc*/
.iwngiV > span{width:inherit;}/*!sc*/
.hMBGua{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.hMBGua:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.hMBGua:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hMBGua:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.hMBGua[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hMBGua[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hMBGua:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hMBGua:active{-webkit-transition:none;transition:none;}/*!sc*/
.hMBGua:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.hMBGua:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hMBGua:focus{outline:solid 1px transparent;}}/*!sc*/
.hMBGua [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hMBGua[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hMBGua[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.hMBGua[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hMBGua[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hMBGua[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hMBGua[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hMBGua[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hMBGua[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hMBGua[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hMBGua[data-block="block"]{width:100%;}/*!sc*/
.hMBGua [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.hMBGua [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hMBGua [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hMBGua [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.hMBGua [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hMBGua [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hMBGua:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.hMBGua:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.hMBGua[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.hMBGua [data-component="leadingVisual"],.hMBGua [data-component="trailingVisual"],.hMBGua [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.hMBGua[data-no-visuals="true"]{border-top-left-radius:0;border-bottom-left-radius:0;display:none;}/*!sc*/
.bDzORU{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.bDzORU:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.bDzORU:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bDzORU:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.bDzORU[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bDzORU[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bDzORU:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bDzORU:active{-webkit-transition:none;transition:none;}/*!sc*/
.bDzORU:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.bDzORU:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bDzORU:focus{outline:solid 1px transparent;}}/*!sc*/
.bDzORU [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bDzORU[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bDzORU[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bDzORU[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bDzORU[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bDzORU[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bDzORU[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bDzORU[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bDzORU[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bDzORU[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bDzORU[data-block="block"]{width:100%;}/*!sc*/
.bDzORU [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.bDzORU [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bDzORU [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bDzORU [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.bDzORU [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bDzORU [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bDzORU:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.bDzORU:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.bDzORU[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.bDzORU [data-component="leadingVisual"],.bDzORU [data-component="trailingVisual"],.bDzORU [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.bDzORU[data-no-visuals="true"]{color:#656d76;}/*!sc*/
.cdPrCH{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.cdPrCH:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.cdPrCH:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.cdPrCH:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.cdPrCH[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.cdPrCH[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cdPrCH:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.cdPrCH:active{-webkit-transition:none;transition:none;}/*!sc*/
.cdPrCH:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.cdPrCH:disabled [data-component=ButtonCounter],.cdPrCH:disabled [data-component="leadingVisual"],.cdPrCH:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.cdPrCH:focus{outline:solid 1px transparent;}}/*!sc*/
.cdPrCH [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cdPrCH[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.cdPrCH[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.cdPrCH[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.cdPrCH[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cdPrCH[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.cdPrCH[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.cdPrCH[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.cdPrCH[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cdPrCH[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.cdPrCH[data-block="block"]{width:100%;}/*!sc*/
.cdPrCH [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.cdPrCH [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.cdPrCH [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.cdPrCH [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.cdPrCH [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.cdPrCH [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cdPrCH:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.cdPrCH:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.cdPrCH[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.cdPrCH[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.cdPrCH[data-no-visuals]{color:#0969da;}/*!sc*/
.cdPrCH:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.cdPrCH:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.cdPrCH:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.cdPrCH[data-size="small"][data-no-visuals="true"]{margin-left:8px;}/*!sc*/
.iUmUix{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#1F2328;background-color:transparent;box-shadow:none;}/*!sc*/
.iUmUix:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iUmUix:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iUmUix:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iUmUix[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iUmUix[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iUmUix:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iUmUix:active{-webkit-transition:none;transition:none;}/*!sc*/
.iUmUix:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.iUmUix:disabled [data-component=ButtonCounter],.iUmUix:disabled [data-component="leadingVisual"],.iUmUix:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iUmUix:focus{outline:solid 1px transparent;}}/*!sc*/
.iUmUix [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iUmUix[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iUmUix[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iUmUix[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iUmUix[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iUmUix[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iUmUix[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iUmUix[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iUmUix[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iUmUix[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iUmUix[data-block="block"]{width:100%;}/*!sc*/
.iUmUix [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.iUmUix [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iUmUix [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iUmUix [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.iUmUix [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iUmUix [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iUmUix:hover:not([disabled]){background-color:#f3f4f6;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iUmUix:active:not([disabled]){background-color:hsla(220,14%,94%,1);-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iUmUix[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.iUmUix[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.iUmUix[data-no-visuals]{color:#0969da;}/*!sc*/
.iUmUix:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.iUmUix:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.iUmUix:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.iUmUix:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gWBIfb{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.gWBIfb:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.gWBIfb:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.gWBIfb:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.gWBIfb[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.gWBIfb[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gWBIfb:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.gWBIfb:active{-webkit-transition:none;transition:none;}/*!sc*/
.gWBIfb:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.gWBIfb:disabled [data-component=ButtonCounter],.gWBIfb:disabled [data-component="leadingVisual"],.gWBIfb:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.gWBIfb:focus{outline:solid 1px transparent;}}/*!sc*/
.gWBIfb [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.gWBIfb[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.gWBIfb[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;color:#1F2328;display:none;}/*!sc*/
.gWBIfb[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.gWBIfb[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.gWBIfb[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.gWBIfb[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
@media screen and (min-width:544px){.gWBIfb[data-size="small"]{display:none;}}/*!sc*/
@media screen and (min-width:768px){.gWBIfb[data-size="small"]{display:block;}}/*!sc*/
@media screen and (min-width:1012px){.gWBIfb[data-size="small"]{display:block;}}/*!sc*/
.gWBIfb[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.gWBIfb[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.gWBIfb[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.gWBIfb[data-block="block"]{width:100%;}/*!sc*/
.gWBIfb [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.gWBIfb [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.gWBIfb [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.gWBIfb [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.gWBIfb [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.gWBIfb [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.gWBIfb:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.gWBIfb:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.gWBIfb[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.gWBIfb[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.gWBIfb[data-no-visuals]{color:#0969da;}/*!sc*/
.gWBIfb:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.gWBIfb:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.gWBIfb:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.iVkWL{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.iVkWL:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iVkWL:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iVkWL:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iVkWL[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iVkWL[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iVkWL:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iVkWL:active{-webkit-transition:none;transition:none;}/*!sc*/
.iVkWL:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.iVkWL:disabled [data-component=ButtonCounter],.iVkWL:disabled [data-component="leadingVisual"],.iVkWL:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iVkWL:focus{outline:solid 1px transparent;}}/*!sc*/
.iVkWL [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iVkWL[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iVkWL[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;color:#1F2328;margin-left:8px;}/*!sc*/
.iVkWL[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iVkWL[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iVkWL[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iVkWL[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iVkWL[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iVkWL[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iVkWL[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iVkWL[data-block="block"]{width:100%;}/*!sc*/
.iVkWL [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.iVkWL [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iVkWL [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iVkWL [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.iVkWL [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iVkWL [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iVkWL:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.iVkWL:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.iVkWL[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.iVkWL[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.iVkWL[data-no-visuals]{color:#0969da;}/*!sc*/
.iVkWL:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.iVkWL:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.iVkWL:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.jxAJvV{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);padding-left:8px;padding-right:8px;}/*!sc*/
.jxAJvV:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.jxAJvV:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jxAJvV:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.jxAJvV[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jxAJvV[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jxAJvV:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jxAJvV:active{-webkit-transition:none;transition:none;}/*!sc*/
.jxAJvV:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.jxAJvV:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jxAJvV:focus{outline:solid 1px transparent;}}/*!sc*/
.jxAJvV [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jxAJvV[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jxAJvV[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jxAJvV[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jxAJvV[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jxAJvV[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jxAJvV[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jxAJvV[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jxAJvV[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jxAJvV[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jxAJvV[data-block="block"]{width:100%;}/*!sc*/
.jxAJvV [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.jxAJvV [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jxAJvV [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jxAJvV [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.jxAJvV [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jxAJvV [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jxAJvV:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.jxAJvV:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.jxAJvV[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.jxAJvV [data-component="leadingVisual"],.jxAJvV [data-component="trailingVisual"],.jxAJvV [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.jxAJvV linkButtonSx:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jxAJvV linkButtonSx:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jxAJvV linkButtonSx:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iCOrao{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.iCOrao:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iCOrao:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iCOrao:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.iCOrao[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iCOrao[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iCOrao:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iCOrao:active{-webkit-transition:none;transition:none;}/*!sc*/
.iCOrao:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.iCOrao:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iCOrao:focus{outline:solid 1px transparent;}}/*!sc*/
.iCOrao [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iCOrao[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iCOrao[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iCOrao[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iCOrao[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iCOrao[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iCOrao[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iCOrao[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iCOrao[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iCOrao[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iCOrao[data-block="block"]{width:100%;}/*!sc*/
.iCOrao [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.iCOrao [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iCOrao [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iCOrao [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.iCOrao [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iCOrao [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iCOrao:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.iCOrao:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.iCOrao[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.iCOrao [data-component="leadingVisual"],.iCOrao [data-component="trailingVisual"],.iCOrao [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.WblXz{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.WblXz:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.WblXz:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.WblXz:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.WblXz[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.WblXz[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.WblXz:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.WblXz:active{-webkit-transition:none;transition:none;}/*!sc*/
.WblXz:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.WblXz:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.WblXz:focus{outline:solid 1px transparent;}}/*!sc*/
.WblXz [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.WblXz[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.WblXz[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.WblXz[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.WblXz[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.WblXz[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.WblXz[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.WblXz[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.WblXz[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.WblXz[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.WblXz[data-block="block"]{width:100%;}/*!sc*/
.WblXz [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.WblXz [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.WblXz [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.WblXz [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.WblXz [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.WblXz [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.WblXz:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.WblXz:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.WblXz[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.WblXz [data-component="leadingVisual"],.WblXz [data-component="trailingVisual"],.WblXz [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.WblXz[data-size="small"][data-no-visuals="true"]{border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.ftQSWB{border-radius:6px;border:1px solid;border-color:rgba(31,35,40,0.15);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#24292f;background-color:#f6f8fa;box-shadow:0 1px 0 rgba(31,35,40,0.04),inset 0 1px 0 rgba(255,255,255,0.25);}/*!sc*/
.ftQSWB:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.ftQSWB:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.ftQSWB:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.ftQSWB[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.ftQSWB[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.ftQSWB:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.ftQSWB:active{-webkit-transition:none;transition:none;}/*!sc*/
.ftQSWB:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.ftQSWB:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.ftQSWB:focus{outline:solid 1px transparent;}}/*!sc*/
.ftQSWB [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ftQSWB[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.ftQSWB[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.ftQSWB[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.ftQSWB[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ftQSWB[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.ftQSWB[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.ftQSWB[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.ftQSWB[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ftQSWB[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.ftQSWB[data-block="block"]{width:100%;}/*!sc*/
.ftQSWB [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.ftQSWB [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.ftQSWB [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.ftQSWB [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.ftQSWB [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.ftQSWB [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ftQSWB:hover:not([disabled]){background-color:#f3f4f6;border-color:rgba(31,35,40,0.15);}/*!sc*/
.ftQSWB:active:not([disabled]){background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.ftQSWB[aria-expanded=true]{background-color:hsla(220,14%,93%,1);border-color:rgba(31,35,40,0.15);}/*!sc*/
.ftQSWB [data-component="leadingVisual"],.ftQSWB [data-component="trailingVisual"],.ftQSWB [data-component="trailingAction"]{color:#656d76;}/*!sc*/
.ftQSWB[data-size="small"][data-no-visuals="true"]{border-top-right-radius:0;border-bottom-right-radius:0;border-right-width:0;}/*!sc*/
.ftQSWB[data-size="small"][data-no-visuals="true"]:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.ftQSWB[data-size="small"][data-no-visuals="true"]:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.ftQSWB[data-size="small"][data-no-visuals="true"]:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hUVEKl{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.hUVEKl:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.hUVEKl:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hUVEKl:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.hUVEKl[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hUVEKl[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hUVEKl:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hUVEKl:active{-webkit-transition:none;transition:none;}/*!sc*/
.hUVEKl:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.hUVEKl:disabled [data-component=ButtonCounter],.hUVEKl:disabled [data-component="leadingVisual"],.hUVEKl:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hUVEKl:focus{outline:solid 1px transparent;}}/*!sc*/
.hUVEKl [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hUVEKl[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hUVEKl[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.hUVEKl[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hUVEKl[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hUVEKl[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hUVEKl[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hUVEKl[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hUVEKl[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hUVEKl[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hUVEKl[data-block="block"]{width:100%;}/*!sc*/
.hUVEKl [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.hUVEKl [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hUVEKl [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hUVEKl [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.hUVEKl [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hUVEKl [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hUVEKl:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.hUVEKl:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.hUVEKl[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.hUVEKl[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.hUVEKl[data-no-visuals]{color:#0969da;}/*!sc*/
.hUVEKl:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.hUVEKl:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.hUVEKl:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.hUVEKl[data-size="small"][data-no-visuals="true"]{color:#656d76;position:relative;}/*!sc*/
.ksLyfZ{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.ksLyfZ:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.ksLyfZ:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.ksLyfZ:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.ksLyfZ[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.ksLyfZ[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.ksLyfZ:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.ksLyfZ:active{-webkit-transition:none;transition:none;}/*!sc*/
.ksLyfZ:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.ksLyfZ:disabled [data-component=ButtonCounter],.ksLyfZ:disabled [data-component="leadingVisual"],.ksLyfZ:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.ksLyfZ:focus{outline:solid 1px transparent;}}/*!sc*/
.ksLyfZ [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ksLyfZ[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.ksLyfZ[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.ksLyfZ[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.ksLyfZ[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ksLyfZ[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.ksLyfZ[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.ksLyfZ[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.ksLyfZ[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ksLyfZ[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.ksLyfZ[data-block="block"]{width:100%;}/*!sc*/
.ksLyfZ [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.ksLyfZ [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.ksLyfZ [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.ksLyfZ [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.ksLyfZ [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.ksLyfZ [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ksLyfZ:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.ksLyfZ:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.ksLyfZ[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.ksLyfZ[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.ksLyfZ[data-no-visuals]{color:#0969da;}/*!sc*/
.ksLyfZ:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.ksLyfZ:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.ksLyfZ:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.ksLyfZ[data-size="small"][data-no-visuals="true"]{color:#656d76;}/*!sc*/
.gmlGme{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#0969da;background-color:transparent;box-shadow:none;}/*!sc*/
.gmlGme:focus:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.gmlGme:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.gmlGme:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #0969da;outline-offset:-2px;}/*!sc*/
.gmlGme[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.gmlGme[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gmlGme:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.gmlGme:active{-webkit-transition:none;transition:none;}/*!sc*/
.gmlGme:disabled{cursor:not-allowed;box-shadow:none;color:#8c959f;}/*!sc*/
.gmlGme:disabled [data-component=ButtonCounter],.gmlGme:disabled [data-component="leadingVisual"],.gmlGme:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.gmlGme:focus{outline:solid 1px transparent;}}/*!sc*/
.gmlGme [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.gmlGme[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.gmlGme[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.gmlGme[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.gmlGme[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.gmlGme[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.gmlGme[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.gmlGme[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.gmlGme[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.gmlGme[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.gmlGme[data-block="block"]{width:100%;}/*!sc*/
.gmlGme [data-component="leadingVisual"]{grid-area:leadingVisual;color:#656d76;}/*!sc*/
.gmlGme [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.gmlGme [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.gmlGme [data-component="trailingAction"]{margin-right:-4px;color:#656d76;}/*!sc*/
.gmlGme [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.gmlGme [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.gmlGme:hover:not([disabled]){background-color:#f3f4f6;}/*!sc*/
.gmlGme:active:not([disabled]){background-color:hsla(220,14%,94%,1);}/*!sc*/
.gmlGme[aria-expanded=true]{background-color:hsla(220,14%,94%,1);}/*!sc*/
.gmlGme[data-component="IconButton"][data-no-visuals]{color:#656d76;}/*!sc*/
.gmlGme[data-no-visuals]{color:#0969da;}/*!sc*/
.gmlGme:has([data-component="ButtonCounter"]){color:#0969da;}/*!sc*/
.gmlGme:disabled[data-no-visuals]{color:#8c959f;}/*!sc*/
.gmlGme:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.gmlGme[data-no-visuals="true"]{-webkit-order:3;-ms-flex-order:3;order:3;color:#1F2328;margin-right:-8px;}/*!sc*/
data-styled.g27[id="types__StyledButton-sc-ws60qy-0"]{content:"iBwhhC,bpzCPD,cpGorR,jOqXES,dQkDZk,iwngiV,hMBGua,bDzORU,cdPrCH,iUmUix,gWBIfb,iVkWL,jxAJvV,iCOrao,WblXz,ftQSWB,hUVEKl,ksLyfZ,gmlGme,"}/*!sc*/
.hFFfJn{position:relative;display:inline-block;}/*!sc*/
.hFFfJn::before{position:absolute;z-index:1000001;display:none;width:0px;height:0px;color:#24292f;pointer-events:none;content:'';border:6px solid transparent;opacity:0;}/*!sc*/
.hFFfJn::after{position:absolute;z-index:1000000;display:none;padding:0.5em 0.75em;font:normal normal 11px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";-webkit-font-smoothing:subpixel-antialiased;color:#ffffff;text-align:center;-webkit-text-decoration:none;text-decoration:none;text-shadow:none;text-transform:none;-webkit-letter-spacing:normal;-moz-letter-spacing:normal;-ms-letter-spacing:normal;letter-spacing:normal;word-wrap:break-word;white-space:pre;pointer-events:none;content:attr(aria-label);background:#24292f;border-radius:3px;opacity:0;}/*!sc*/
@-webkit-keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
@keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
.hFFfJn:hover::before,.hFFfJn:active::before,.hFFfJn:focus::before,.hFFfJn:focus-within::before,.hFFfJn:hover::after,.hFFfJn:active::after,.hFFfJn:focus::after,.hFFfJn:focus-within::after{display:inline-block;-webkit-text-decoration:none;text-decoration:none;-webkit-animation-name:tooltip-appear;animation-name:tooltip-appear;-webkit-animation-duration:0.1s;animation-duration:0.1s;-webkit-animation-fill-mode:forwards;animation-fill-mode:forwards;-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-animation-delay:0.4s;animation-delay:0.4s;}/*!sc*/
.hFFfJn.tooltipped-no-delay:hover::before,.hFFfJn.tooltipped-no-delay:active::before,.hFFfJn.tooltipped-no-delay:focus::before,.hFFfJn.tooltipped-no-delay:focus-within::before,.hFFfJn.tooltipped-no-delay:hover::after,.hFFfJn.tooltipped-no-delay:active::after,.hFFfJn.tooltipped-no-delay:focus::after,.hFFfJn.tooltipped-no-delay:focus-within::after{-webkit-animation-delay:0s;animation-delay:0s;}/*!sc*/
.hFFfJn.tooltipped-multiline:hover::after,.hFFfJn.tooltipped-multiline:active::after,.hFFfJn.tooltipped-multiline:focus::after,.hFFfJn.tooltipped-multiline:focus-within::after{display:table-cell;}/*!sc*/
.hFFfJn.tooltipped-s::after,.hFFfJn.tooltipped-se::after,.hFFfJn.tooltipped-sw::after{top:100%;right:50%;margin-top:6px;}/*!sc*/
.hFFfJn.tooltipped-s::before,.hFFfJn.tooltipped-se::before,.hFFfJn.tooltipped-sw::before{top:auto;right:50%;bottom:-7px;margin-right:-6px;border-bottom-color:#24292f;}/*!sc*/
.hFFfJn.tooltipped-se::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.hFFfJn.tooltipped-sw::after{margin-right:-16px;}/*!sc*/
.hFFfJn.tooltipped-n::after,.hFFfJn.tooltipped-ne::after,.hFFfJn.tooltipped-nw::after{right:50%;bottom:100%;margin-bottom:6px;}/*!sc*/
.hFFfJn.tooltipped-n::before,.hFFfJn.tooltipped-ne::before,.hFFfJn.tooltipped-nw::before{top:-7px;right:50%;bottom:auto;margin-right:-6px;border-top-color:#24292f;}/*!sc*/
.hFFfJn.tooltipped-ne::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.hFFfJn.tooltipped-nw::after{margin-right:-16px;}/*!sc*/
.hFFfJn.tooltipped-s::after,.hFFfJn.tooltipped-n::after{-webkit-transform:translateX(50%);-ms-transform:translateX(50%);transform:translateX(50%);}/*!sc*/
.hFFfJn.tooltipped-w::after{right:100%;bottom:50%;margin-right:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.hFFfJn.tooltipped-w::before{top:50%;bottom:50%;left:-7px;margin-top:-6px;border-left-color:#24292f;}/*!sc*/
.hFFfJn.tooltipped-e::after{bottom:50%;left:100%;margin-left:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.hFFfJn.tooltipped-e::before{top:50%;right:-7px;bottom:50%;margin-top:-6px;border-right-color:#24292f;}/*!sc*/
.hFFfJn.tooltipped-multiline::after{width:-webkit-max-content;width:-moz-max-content;width:max-content;max-width:250px;word-wrap:break-word;white-space:pre-line;border-collapse:separate;}/*!sc*/
.hFFfJn.tooltipped-multiline.tooltipped-s::after,.hFFfJn.tooltipped-multiline.tooltipped-n::after{right:auto;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);}/*!sc*/
.hFFfJn.tooltipped-multiline.tooltipped-w::after,.hFFfJn.tooltipped-multiline.tooltipped-e::after{right:100%;}/*!sc*/
.hFFfJn.tooltipped-align-right-2::after{right:0;margin-right:0;}/*!sc*/
.hFFfJn.tooltipped-align-right-2::before{right:15px;}/*!sc*/
.hFFfJn.tooltipped-align-left-2::after{left:0;margin-left:0;}/*!sc*/
.hFFfJn.tooltipped-align-left-2::before{left:10px;}/*!sc*/
data-styled.g28[id="Tooltip__TooltipBase-sc-uha8qm-0"]{content:"hFFfJn,"}/*!sc*/
.cDLBls{border:0;font-size:inherit;font-family:inherit;background-color:transparent;-webkit-appearance:none;color:inherit;width:100%;}/*!sc*/
.cDLBls:focus{outline:0;}/*!sc*/
data-styled.g29[id="UnstyledTextInput-sc-14ypya-0"]{content:"cDLBls,"}/*!sc*/
.bOMzPg{min-width:0;}/*!sc*/
.ivLLle{padding-left:4px;padding-right:4px;font-weight:400;color:#656d76;font-size:16px;}/*!sc*/
.ghRVGj{color:#1F2328;}/*!sc*/
.dZAxGI{padding-left:4px;padding-right:4px;font-weight:400;color:#656d76;font-size:14px;}/*!sc*/
data-styled.g35[id="Text-sc-17v1xeu-0"]{content:"bOMzPg,ivLLle,ghRVGj,gPDEWA,dZAxGI,"}/*!sc*/
.cjbBGq{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle;isolation:isolate;}/*!sc*/
.cjbBGq.cjbBGq > *{margin-inline-end:-1px;position:relative;border-radius:0;}/*!sc*/
.cjbBGq.cjbBGq > *:first-child{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:last-child{border-top-right-radius:6px;border-bottom-right-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:focus,.cjbBGq.cjbBGq > *:active,.cjbBGq.cjbBGq > *:hover{z-index:1;}/*!sc*/
data-styled.g84[id="ButtonGroup-sc-1gxhls1-0"]{content:"cjbBGq,"}/*!sc*/
.iQDIzE{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:600;padding:0;height:100%;width:100%;}/*!sc*/
.iQDIzE .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:#ffffff;border-color:#8c959f;border-style:solid;border-width:1px;border-radius:var(--segmented-control-outer-radius);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:var(--segmented-control-button-inner-padding);padding-right:var(--segmented-control-button-inner-padding);}/*!sc*/
.iQDIzE svg{fill:#656d76;}/*!sc*/
.iQDIzE:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.iQDIzE .segmentedControl-text:after{content:"Code";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.iQDIzE:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
.hBvGcq{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:400;padding:var(--segmented-control-button-bg-inset);height:100%;width:100%;}/*!sc*/
.hBvGcq .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:transparent;border-color:transparent;border-style:solid;border-width:1px;border-radius:calc(var(--segmented-control-outer-radius) - var(--segmented-control-button-bg-inset) / 2);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));padding-right:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));}/*!sc*/
.hBvGcq svg{fill:#656d76;}/*!sc*/
.hBvGcq:hover .segmentedControl-content{background-color:rgba(175,184,193,0.2);}/*!sc*/
.hBvGcq:active .segmentedControl-content{background-color:rgba(175,184,193,0.4);}/*!sc*/
.hBvGcq:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.hBvGcq .segmentedControl-text:after{content:"Blame";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.hBvGcq:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
data-styled.g91[id="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0"]{content:"iQDIzE,hBvGcq,"}/*!sc*/
.iYVwMz{background-color:#eaeef2;border-radius:6px;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;font-size:14px;height:28px;margin:0;padding:0;}/*!sc*/
data-styled.g93[id="SegmentedControl__SegmentedControlList-sc-1rzig82-0"]{content:"iYVwMz,"}/*!sc*/
body[data-page-layout-dragging="true"]{cursor:col-resize;}/*!sc*/
body[data-page-layout-dragging="true"] *{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}/*!sc*/
data-styled.g97[id="sc-global-gbKrvU1"]{content:"sc-global-gbKrvU1,"}/*!sc*/
.gtekST{list-style:none;padding:0;margin:0;}/*!sc*/
.gtekST .PRIVATE_TreeView-item{outline:none;}/*!sc*/
.gtekST .PRIVATE_TreeView-item:focus-visible > div,.gtekST .PRIVATE_TreeView-item.focus-visible > div{box-shadow:inset 0 0 0 2px #0969da;}/*!sc*/
@media (forced-colors:active){.gtekST .PRIVATE_TreeView-item:focus-visible > div,.gtekST .PRIVATE_TreeView-item.focus-visible > div{outline:2px solid HighlightText;outline-offset:-2;}}/*!sc*/
.gtekST .PRIVATE_TreeView-item-container{--level:1;--toggle-width:1rem;position:relative;display:grid;grid-template-columns:calc(calc(var(--level) - 1) * (var(--toggle-width) / 2)) var(--toggle-width) 1fr;grid-template-areas:'spacer toggle content';width:100%;min-height:2rem;font-size:14px;color:#1F2328;border-radius:6px;cursor:pointer;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-container:hover{background-color:rgba(208,215,222,0.32);}/*!sc*/
@media (forced-colors:active){.gtekST .PRIVATE_TreeView-item-container:hover{outline:2px solid transparent;outline-offset:-2px;}}/*!sc*/
@media (pointer:coarse){.gtekST .PRIVATE_TreeView-item-container{--toggle-width:1.5rem;min-height:2.75rem;}}/*!sc*/
.gtekST .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{background-color:transparent;cursor:default;}/*!sc*/
@media (forced-colors:active){.gtekST .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{outline:none;}}/*!sc*/
.gtekST[data-omit-spacer='true'] .PRIVATE_TreeView-item-container{grid-template-columns:0 0 1fr;}/*!sc*/
.gtekST .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container{background-color:rgba(208,215,222,0.24);}/*!sc*/
.gtekST .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{content:'';position:absolute;top:calc(50% - 0.75rem);left:-8px;width:0.25rem;height:1.5rem;background-color:#0969da;border-radius:6px;}/*!sc*/
@media (forced-colors:active){.gtekST .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{background-color:HighlightText;}}/*!sc*/
.gtekST .PRIVATE_TreeView-item-toggle{grid-area:toggle;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;height:100%;color:#656d76;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-toggle--hover:hover{background-color:rgba(208,215,222,0.32);}/*!sc*/
.gtekST .PRIVATE_TreeView-item-toggle--end{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-content{grid-area:content;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:100%;padding:0 8px;gap:8px;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-content-text{-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-visual{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;color:#656d76;}/*!sc*/
.gtekST .PRIVATE_TreeView-item-level-line{width:100%;height:100%;border-right:1px solid;border-color:rgba(31,35,40,0.15);}/*!sc*/
@media (hover:hover){.gtekST .PRIVATE_TreeView-item-level-line{border-color:transparent;}.gtekST:hover .PRIVATE_TreeView-item-level-line,.gtekST:focus-within .PRIVATE_TreeView-item-level-line{border-color:rgba(31,35,40,0.15);}}/*!sc*/
.gtekST .PRIVATE_TreeView-directory-icon{display:grid;color:#54aeff;}/*!sc*/
.gtekST .PRIVATE_VisuallyHidden{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g104[id="TreeView__UlBox-sc-4ex6b6-0"]{content:"gtekST,"}/*!sc*/
</style><meta data-hydrostats="publish"/> <!-- --> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-g0xbh4-0"><div style="--sticky-pane-height:100vh" class="Box-sc-g0xbh4-0 fSWWem"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 kFEKvZ"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div class="Box-sc-g0xbh4-0 hAeDYA"><div role="separator" class="Box-sc-g0xbh4-0 ekKrwo"></div></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 gNdDUH"><span class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"><form><label for=":Rdjal5:-width-input">Pane width</label><p id=":Rdjal5:-input-hint">Use a value between <!-- -->0<!-- -->% and <!-- -->0<!-- -->%</p><input id=":Rdjal5:-width-input" aria-describedby=":Rdjal5:-input-hint" name="pane-width" inputMode="numeric" pattern="[0-9]*" autoCorrect="off" autoComplete="off" type="text" value=""/><button type="submit">Change width</button></form></span><div class="Box-sc-g0xbh4-0 react-tree-pane-contents-3-panel"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jywUSN"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 iBwhhC"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 bpzCPD" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 cpGorR react-repos-tree-pane-ref-selector width-full ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 kYlvBX"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-uha8qm-0 hFFfJn tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jOqXES" href="/paulog16/Programacion1/new/main"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dQkDZk"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="Box-sc-g0xbh4-0 ccToMy"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 cgNHBf cuQjCh TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autoCorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""/><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 cLfAnm"><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 gtekST"><li class="PRIVATE_TreeView-item" tabindex="0" id="Trabajo_practico_5-item" role="treeitem" aria-labelledby=":Rqcndjal5:" aria-describedby=":Rqcndjal5H1: :Rqcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>Trabajo_practico_5</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Ejercicio Complementario1.py-item" role="treeitem" aria-labelledby=":R1acndjal5:" aria-describedby=":R1acndjal5H1: :R1acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Ejercicio Complementario1.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Ejercicios en clase – Variables dimensionadas.py-item" role="treeitem" aria-labelledby=":R1qcndjal5:" aria-describedby=":R1qcndjal5H1: :R1qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Ejercicios en clase – Variables dimensionadas.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Trabajo Práctico Nro 1 -Programación 1 - (2) (2).docx-item" role="treeitem" aria-labelledby=":R2acndjal5:" aria-describedby=":R2acndjal5H1: :R2acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Trabajo Práctico Nro 1 -Programación 1 - (2) (2).docx</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Trabajo-Practico-n2.py-item" role="treeitem" aria-labelledby=":R2qcndjal5:" aria-describedby=":R2qcndjal5H1: :R2qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Trabajo-Practico-n2.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Trabajo_Practico_Nro1_Parte2_Programacion.py-item" role="treeitem" aria-labelledby=":R3acndjal5:" aria-describedby=":R3acndjal5H1: :R3acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Trabajo_Practico_Nro1_Parte2_Programacion.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="Trabajo_práctico_nro6.py-item" role="treeitem" aria-labelledby=":R3qcndjal5:" aria-describedby=":R3qcndjal5H1: :R3qcndjal5H2:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Trabajo_práctico_nro6.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="ahorcado.py-item" role="treeitem" aria-labelledby=":R4acndjal5:" aria-describedby=":R4acndjal5H1: :R4acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>ahorcado.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="ejercicio_ciclos.py-item" role="treeitem" aria-labelledby=":R4qcndjal5:" aria-describedby=":R4qcndjal5H1: :R4qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>ejercicio_ciclos.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="ejercicio_clase_variables_dimensionales.py-item" role="treeitem" aria-labelledby=":R5acndjal5:" aria-describedby=":R5acndjal5H1: :R5acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>ejercicio_clase_variables_dimensionales.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="funciones.py-item" role="treeitem" aria-labelledby=":R5qcndjal5:" aria-describedby=":R5qcndjal5H1: :R5qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>funciones.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="repaso.py-item" role="treeitem" aria-labelledby=":R6acndjal5:" aria-describedby=":R6acndjal5H1: :R6acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R6acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>repaso.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="repaso2.py-item" role="treeitem" aria-labelledby=":R6qcndjal5:" aria-describedby=":R6qcndjal5H1: :R6qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R6qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>repaso2.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="tp_funciones.py-item" role="treeitem" aria-labelledby=":R7acndjal5:" aria-describedby=":R7acndjal5H1: :R7acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R7acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>tp_funciones.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="trabajo-condicionales.py-item" role="treeitem" aria-labelledby=":R7qcndjal5:" aria-describedby=":R7qcndjal5H1: :R7qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R7qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>trabajo-condicionales.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="trabajo_Practico3.py-item" role="treeitem" aria-labelledby=":R8acndjal5:" aria-describedby=":R8acndjal5H1: :R8acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R8acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>trabajo_Practico3.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="trabajo_practico_nro4.py-item" role="treeitem" aria-labelledby=":R8qcndjal5:" aria-describedby=":R8qcndjal5H1: :R8qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R8qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>trabajo_practico_nro4.py</span></span></div></div></li></ul></nav></div></div><div class="Box-sc-g0xbh4-0 hwhShM"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 fIqerb">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 fIqerb">Share feedback</a></div></div></div><div class="Box-sc-g0xbh4-0 fBtiVT"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 fIqerb">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 fIqerb">Share feedback</a></div></div></div></div></div></div></div><main class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="Box-sc-g0xbh4-0 kgXdnT react-code-view-header--narrow"><div class="Box-sc-g0xbh4-0 kzTa-dF"><div class="Box-sc-g0xbh4-0 bbXCl"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 iBwhhC"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 bpzCPD" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><div class="Box-sc-g0xbh4-0 hGGMNu"><div class="Box-sc-g0xbh4-0 eHRrYV"><button type="button" id="branch-picker-repos-header-ref-selector-narrow" aria-haspopup="true" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 iwngiV ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 kYlvBX"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dKmYfk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hMBGua"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 bDzORU js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9aaqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div><div class="Box-sc-g0xbh4-0 hSNzKh"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-mobile-heading" id="repos-header-breadcrumb-mobile" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-mobile-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 eVjWum" href="/paulog16/Programacion1/tree/main">Programacion1</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ivLLle">/</span><h1 tabindex="-1" id="file-name-id-mobile" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">Trabajo_práctico_nro6.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 cdPrCH"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div></div><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs react-code-view-header--wide"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-wide-heading" id="repos-header-breadcrumb-wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 eVjWum" href="/paulog16/Programacion1/tree/main">Programacion1</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ivLLle">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">Trabajo_práctico_nro6.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 cdPrCH"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hMBGua"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 bDzORU js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9pkqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MERGN react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div><div class="Box-sc-g0xbh4-0"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 MERGN"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-g0xbh4-0 kLxXov"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="Box-sc-g0xbh4-0 jGfYmh"><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"></div><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 iUmUix react-last-commit-history-group" href="/paulog16/Programacion1/commits/main/Trabajo_pr%C3%A1ctico_nro6.py" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 ghRVGj">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"></div><span role="tooltip" aria-label="Commit history" class="Tooltip__TooltipBase-sc-uha8qm-0 hFFfJn tooltipped-n"><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 iUmUix react-last-commit-history-icon" href="/paulog16/Programacion1/commits/main/Trabajo_pr%C3%A1ctico_nro6.py"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 kjydbF container"><div class="Box-sc-g0xbh4-0 bSdwWB react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 bZpGqz text-mono"><div title="5.98 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">180 lines (159 loc) · 5.98 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-banner"><button type="button" id=":R2bqlajal5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 gWBIfb"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6.25 9a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 6.25 9Zm4.25.75a.75.75 0 0 0-1.5 0v1.5a.75.75 0 0 0 1.5 0v-1.5Z"></path><path d="M7.86 1.77c.05.053.097.107.14.164.043-.057.09-.111.14-.164.681-.731 1.737-.9 2.943-.765 1.23.136 2.145.527 2.724 1.26.566.716.693 1.614.693 2.485 0 .572-.053 1.147-.254 1.655l.168.838.066.033A2.75 2.75 0 0 1 16 9.736V11c0 .24-.086.438-.156.567-.073.131-.16.253-.259.366-.18.21-.404.413-.605.58a10.19 10.19 0 0 1-.792.597l-.015.01-.006.004-.028.018a8.849 8.849 0 0 1-.456.281c-.307.177-.749.41-1.296.642C11.296 14.528 9.756 15 8 15c-1.756 0-3.296-.472-4.387-.935a12.28 12.28 0 0 1-1.296-.641 8.849 8.849 0 0 1-.456-.281l-.028-.02-.006-.003-.015-.01a10.593 10.593 0 0 1-.792-.596 5.264 5.264 0 0 1-.605-.58 2.133 2.133 0 0 1-.259-.367A1.189 1.189 0 0 1 0 11V9.736a2.75 2.75 0 0 1 1.52-2.46l.067-.033.167-.838C1.553 5.897 1.5 5.322 1.5 4.75c0-.87.127-1.77.693-2.485.579-.733 1.494-1.124 2.724-1.26 1.206-.134 2.262.034 2.944.765ZM3 7.824v4.261c.02.013.043.025.065.038.264.152.65.356 1.134.562.972.412 2.307.815 3.801.815 1.494 0 2.83-.403 3.8-.815.412-.174.813-.375 1.2-.6v-4.26l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.06-.328-2.71-.991A3.233 3.233 0 0 1 8 6.266c-.144.269-.321.52-.54.743C6.81 7.672 5.896 8 4.75 8c-.652 0-1.236-.082-1.726-.291L3 7.824Zm6.237-5.031c-.204.218-.359.678-.242 1.614.091.726.303 1.23.618 1.553.299.304.784.54 1.638.54.922 0 1.28-.199 1.442-.38.179-.2.308-.578.308-1.37 0-.765-.123-1.242-.37-1.555-.233-.296-.693-.586-1.713-.7-1.044-.116-1.488.091-1.681.298Zm-2.472 0c-.193-.207-.637-.414-1.681-.298-1.02.114-1.48.404-1.713.7-.247.313-.37.79-.37 1.555 0 .792.129 1.17.308 1.37.162.181.52.38 1.442.38.854 0 1.339-.236 1.638-.54.315-.323.527-.827.618-1.553.117-.936-.038-1.396-.242-1.614Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 gBKNLX react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 eVjWum" href="/paulog16/Programacion1/tree/main">Programacion1</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 dZAxGI">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">Trabajo_práctico_nro6.py</h1></div></div><button type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 iVkWL"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 bvEDG"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 iYVwMz"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 iQDIzE"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 jkTWSe"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 hBvGcq"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 bZpGqz text-mono"><div title="5.98 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">180 lines (159 loc) · 5.98 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-in-header"><button type="button" id=":R79jqlajal5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 gWBIfb"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6.25 9a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 6.25 9Zm4.25.75a.75.75 0 0 0-1.5 0v1.5a.75.75 0 0 0 1.5 0v-1.5Z"></path><path d="M7.86 1.77c.05.053.097.107.14.164.043-.057.09-.111.14-.164.681-.731 1.737-.9 2.943-.765 1.23.136 2.145.527 2.724 1.26.566.716.693 1.614.693 2.485 0 .572-.053 1.147-.254 1.655l.168.838.066.033A2.75 2.75 0 0 1 16 9.736V11c0 .24-.086.438-.156.567-.073.131-.16.253-.259.366-.18.21-.404.413-.605.58a10.19 10.19 0 0 1-.792.597l-.015.01-.006.004-.028.018a8.849 8.849 0 0 1-.456.281c-.307.177-.749.41-1.296.642C11.296 14.528 9.756 15 8 15c-1.756 0-3.296-.472-4.387-.935a12.28 12.28 0 0 1-1.296-.641 8.849 8.849 0 0 1-.456-.281l-.028-.02-.006-.003-.015-.01a10.593 10.593 0 0 1-.792-.596 5.264 5.264 0 0 1-.605-.58 2.133 2.133 0 0 1-.259-.367A1.189 1.189 0 0 1 0 11V9.736a2.75 2.75 0 0 1 1.52-2.46l.067-.033.167-.838C1.553 5.897 1.5 5.322 1.5 4.75c0-.87.127-1.77.693-2.485.579-.733 1.494-1.124 2.724-1.26 1.206-.134 2.262.034 2.944.765ZM3 7.824v4.261c.02.013.043.025.065.038.264.152.65.356 1.134.562.972.412 2.307.815 3.801.815 1.494 0 2.83-.403 3.8-.815.412-.174.813-.375 1.2-.6v-4.26l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.06-.328-2.71-.991A3.233 3.233 0 0 1 8 6.266c-.144.269-.321.52-.54.743C6.81 7.672 5.896 8 4.75 8c-.652 0-1.236-.082-1.726-.291L3 7.824Zm6.237-5.031c-.204.218-.359.678-.242 1.614.091.726.303 1.23.618 1.553.299.304.784.54 1.638.54.922 0 1.28-.199 1.442-.38.179-.2.308-.578.308-1.37 0-.765-.123-1.242-.37-1.555-.233-.296-.693-.586-1.713-.7-1.044-.116-1.488.091-1.681.298Zm-2.472 0c-.193-.207-.637-.414-1.681-.298-1.02.114-1.48.404-1.713.7-.247.313-.37.79-.37 1.555 0 .792.129 1.17.308 1.37.162.181.52.38 1.442.38.854 0 1.339-.236 1.638-.54.315-.323.527-.827.618-1.553.117-.936-.038-1.396-.242-1.614Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/paulog16/Programacion1/raw/main/Trabajo_pr%C3%A1ctico_nro6.py" data-testid="raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jxAJvV"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iCOrao"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" class="Tooltip__TooltipBase-sc-uha8qm-0 hFFfJn tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 WblXz"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 fIqerb js-github-dev-shortcut d-none" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 fIqerb js-github-dev-new-tab-shortcut d-none" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="Fork this repository and edit the file" class="Tooltip__TooltipBase-sc-uha8qm-0 hFFfJn tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 ftQSWB" href="/paulog16/Programacion1/edit/main/Trabajo_pr%C3%A1ctico_nro6.py"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":Rl7pjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iCOrao"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,E" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Close symbols panel" class="Tooltip__TooltipBase-sc-uha8qm-0 hFFfJn tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="true" aria-expanded="true" aria-controls="symbols-pane" class="types__StyledButton-sc-ws60qy-0 hUVEKl" data-testid="symbols-button" id="symbols-button" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 ksLyfZ js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R1dpjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></div><div class="Box-sc-g0xbh4-0 flDsrw"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 jWnGGx"><div class="Box-sc-g0xbh4-0 TCenl"><div id="highlighted-line-menu-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div class="Box-sc-g0xbh4-0 eRkHwF"><div class="Box-sc-g0xbh4-0 knCTAx react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers" style="pointer-events:auto"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right:16px">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right:16px">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right:16px">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right:16px">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right:16px">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right:16px">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right:16px">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right:16px">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right:16px">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right:16px">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right:16px">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right:16px">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right:16px">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right:16px">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right:16px">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right:16px">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right:16px">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right:16px">18</div><div data-line-number="19" class="react-line-number react-code-text" style="padding-right:16px">19</div><div data-line-number="20" class="react-line-number react-code-text" style="padding-right:16px">20</div><div data-line-number="21" class="react-line-number react-code-text" style="padding-right:16px">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right:16px">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right:16px">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right:16px">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right:16px">25</div><div data-line-number="26" class="react-line-number react-code-text" style="padding-right:16px">26</div><div data-line-number="27" class="react-line-number react-code-text" style="padding-right:16px">27</div><div data-line-number="28" class="react-line-number react-code-text" style="padding-right:16px">28</div><div data-line-number="29" class="react-line-number react-code-text" style="padding-right:16px">29</div><div data-line-number="30" class="react-line-number react-code-text" style="padding-right:16px">30</div><div data-line-number="31" class="react-line-number react-code-text" style="padding-right:16px">31</div><div data-line-number="32" class="react-line-number react-code-text" style="padding-right:16px">32</div><div data-line-number="33" class="react-line-number react-code-text" style="padding-right:16px">33</div><div data-line-number="34" class="react-line-number react-code-text" style="padding-right:16px">34</div><div data-line-number="35" class="react-line-number react-code-text" style="padding-right:16px">35</div><div data-line-number="36" class="react-line-number react-code-text" style="padding-right:16px">36</div><div data-line-number="37" class="react-line-number react-code-text" style="padding-right:16px">37</div><div data-line-number="38" class="react-line-number react-code-text" style="padding-right:16px">38</div><div data-line-number="39" class="react-line-number react-code-text" style="padding-right:16px">39</div><div data-line-number="40" class="react-line-number react-code-text" style="padding-right:16px">40</div><div data-line-number="41" class="react-line-number react-code-text" style="padding-right:16px">41</div><div data-line-number="42" class="react-line-number react-code-text" style="padding-right:16px">42</div><div data-line-number="43" class="react-line-number react-code-text" style="padding-right:16px">43</div><div data-line-number="44" class="react-line-number react-code-text" style="padding-right:16px">44</div><div data-line-number="45" class="react-line-number react-code-text" style="padding-right:16px">45</div><div data-line-number="46" class="react-line-number react-code-text" style="padding-right:16px">46</div><div data-line-number="47" class="react-line-number react-code-text" style="padding-right:16px">47</div><div data-line-number="48" class="react-line-number react-code-text" style="padding-right:16px">48</div><div data-line-number="49" class="react-line-number react-code-text" style="padding-right:16px">49</div><div data-line-number="50" class="react-line-number react-code-text" style="padding-right:16px">50</div><div data-line-number="51" class="react-line-number react-code-text" style="padding-right:16px">51</div><div data-line-number="52" class="react-line-number react-code-text" style="padding-right:16px">52</div><div data-line-number="53" class="react-line-number react-code-text" style="padding-right:16px">53</div><div data-line-number="54" class="react-line-number react-code-text" style="padding-right:16px">54</div><div data-line-number="55" class="react-line-number react-code-text" style="padding-right:16px">55</div><div data-line-number="56" class="react-line-number react-code-text" style="padding-right:16px">56</div><div data-line-number="57" class="react-line-number react-code-text" style="padding-right:16px">57</div><div data-line-number="58" class="react-line-number react-code-text" style="padding-right:16px">58</div><div data-line-number="59" class="react-line-number react-code-text" style="padding-right:16px">59</div><div data-line-number="60" class="react-line-number react-code-text" style="padding-right:16px">60</div><div data-line-number="61" class="react-line-number react-code-text" style="padding-right:16px">61</div><div data-line-number="62" class="react-line-number react-code-text" style="padding-right:16px">62</div><div data-line-number="63" class="react-line-number react-code-text" style="padding-right:16px">63</div><div data-line-number="64" class="react-line-number react-code-text" style="padding-right:16px">64</div><div data-line-number="65" class="react-line-number react-code-text" style="padding-right:16px">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right:16px">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right:16px">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right:16px">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right:16px">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right:16px">70</div><div data-line-number="71" class="react-line-number react-code-text" style="padding-right:16px">71</div><div data-line-number="72" class="react-line-number react-code-text" style="padding-right:16px">72</div><div data-line-number="73" class="react-line-number react-code-text" style="padding-right:16px">73</div><div data-line-number="74" class="react-line-number react-code-text" style="padding-right:16px">74</div><div data-line-number="75" class="react-line-number react-code-text" style="padding-right:16px">75</div><div data-line-number="76" class="react-line-number react-code-text" style="padding-right:16px">76</div><div data-line-number="77" class="react-line-number react-code-text" style="padding-right:16px">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right:16px">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right:16px">79</div><div data-line-number="80" class="react-line-number react-code-text" style="padding-right:16px">80</div><div data-line-number="81" class="react-line-number react-code-text" style="padding-right:16px">81</div><div data-line-number="82" class="react-line-number react-code-text" style="padding-right:16px">82</div><div data-line-number="83" class="react-line-number react-code-text" style="padding-right:16px">83</div><div data-line-number="84" class="react-line-number react-code-text" style="padding-right:16px">84</div><div data-line-number="85" class="react-line-number react-code-text" style="padding-right:16px">85</div><div data-line-number="86" class="react-line-number react-code-text" style="padding-right:16px">86</div><div data-line-number="87" class="react-line-number react-code-text" style="padding-right:16px">87</div><div data-line-number="88" class="react-line-number react-code-text" style="padding-right:16px">88</div><div data-line-number="89" class="react-line-number react-code-text" style="padding-right:16px">89</div><div data-line-number="90" class="react-line-number react-code-text" style="padding-right:16px">90</div><div data-line-number="91" class="react-line-number react-code-text" style="padding-right:16px">91</div><div data-line-number="92" class="react-line-number react-code-text" style="padding-right:16px">92</div><div data-line-number="93" class="react-line-number react-code-text" style="padding-right:16px">93</div><div data-line-number="94" class="react-line-number react-code-text" style="padding-right:16px">94</div><div data-line-number="95" class="react-line-number react-code-text" style="padding-right:16px">95</div><div data-line-number="96" class="react-line-number react-code-text" style="padding-right:16px">96</div><div data-line-number="97" class="react-line-number react-code-text" style="padding-right:16px">97</div><div data-line-number="98" class="react-line-number react-code-text" style="padding-right:16px">98</div><div data-line-number="99" class="react-line-number react-code-text" style="padding-right:16px">99</div><div data-line-number="100" class="react-line-number react-code-text" style="padding-right:16px">100</div><div data-line-number="101" class="react-line-number react-code-text" style="padding-right:16px">101</div><div data-line-number="102" class="react-line-number react-code-text" style="padding-right:16px">102</div><div data-line-number="103" class="react-line-number react-code-text" style="padding-right:16px">103</div><div data-line-number="104" class="react-line-number react-code-text" style="padding-right:16px">104</div><div data-line-number="105" class="react-line-number react-code-text" style="padding-right:16px">105</div><div data-line-number="106" class="react-line-number react-code-text" style="padding-right:16px">106</div><div data-line-number="107" class="react-line-number react-code-text" style="padding-right:16px">107</div><div data-line-number="108" class="react-line-number react-code-text" style="padding-right:16px">108</div><div data-line-number="109" class="react-line-number react-code-text" style="padding-right:16px">109</div><div data-line-number="110" class="react-line-number react-code-text" style="padding-right:16px">110<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="111" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">111</div><div data-line-number="112" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">112</div><div data-line-number="113" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">113</div><div data-line-number="114" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">114</div><div data-line-number="115" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">115</div><div data-line-number="116" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">116</div><div data-line-number="117" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">117</div><div data-line-number="118" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">118</div><div data-line-number="119" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">119</div><div data-line-number="120" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">120</div><div data-line-number="121" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">121</div><div data-line-number="122" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">122</div><div data-line-number="123" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">123</div><div data-line-number="124" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">124</div><div data-line-number="125" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">125</div><div data-line-number="126" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">126</div><div data-line-number="127" class="child-of-line-110  react-line-number react-code-text" style="padding-right:16px">127</div><div data-line-number="128" class="react-line-number react-code-text" style="padding-right:16px">128</div><div data-line-number="129" class="react-line-number react-code-text" style="padding-right:16px">129</div><div data-line-number="130" class="react-line-number react-code-text" style="padding-right:16px">130</div><div data-line-number="131" class="react-line-number react-code-text" style="padding-right:16px">131<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="132" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">132</div><div data-line-number="133" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">133</div><div data-line-number="134" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">134</div><div data-line-number="135" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">135</div><div data-line-number="136" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">136</div><div data-line-number="137" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">137</div><div data-line-number="138" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">138</div><div data-line-number="139" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">139</div><div data-line-number="140" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">140</div><div data-line-number="141" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">141</div><div data-line-number="142" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">142</div><div data-line-number="143" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">143</div><div data-line-number="144" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">144</div><div data-line-number="145" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">145</div><div data-line-number="146" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">146</div><div data-line-number="147" class="child-of-line-131  react-line-number react-code-text" style="padding-right:16px">147</div><div data-line-number="148" class="react-line-number react-code-text" style="padding-right:16px">148</div><div data-line-number="149" class="react-line-number react-code-text" style="padding-right:16px">149</div><div data-line-number="150" class="react-line-number react-code-text" style="padding-right:16px">150</div><div data-line-number="151" class="react-line-number react-code-text" style="padding-right:16px">151</div><div data-line-number="152" class="react-line-number react-code-text" style="padding-right:16px">152</div><div data-line-number="153" class="react-line-number react-code-text" style="padding-right:16px">153</div><div data-line-number="154" class="react-line-number react-code-text" style="padding-right:16px">154</div><div data-line-number="155" class="react-line-number react-code-text" style="padding-right:16px">155</div><div data-line-number="156" class="react-line-number react-code-text" style="padding-right:16px">156</div><div data-line-number="157" class="react-line-number react-code-text" style="padding-right:16px">157</div><div data-line-number="158" class="react-line-number react-code-text" style="padding-right:16px">158</div><div data-line-number="159" class="react-line-number react-code-text" style="padding-right:16px">159</div><div data-line-number="160" class="react-line-number react-code-text" style="padding-right:16px">160</div><div data-line-number="161" class="react-line-number react-code-text" style="padding-right:16px">161</div><div data-line-number="162" class="react-line-number react-code-text" style="padding-right:16px">162</div><div data-line-number="163" class="react-line-number react-code-text" style="padding-right:16px">163</div><div data-line-number="164" class="react-line-number react-code-text" style="padding-right:16px">164</div><div data-line-number="165" class="react-line-number react-code-text" style="padding-right:16px">165</div><div data-line-number="166" class="react-line-number react-code-text" style="padding-right:16px">166</div><div data-line-number="167" class="react-line-number react-code-text" style="padding-right:16px">167</div><div data-line-number="168" class="react-line-number react-code-text" style="padding-right:16px">168</div><div data-line-number="169" class="react-line-number react-code-text" style="padding-right:16px">169</div><div data-line-number="170" class="react-line-number react-code-text" style="padding-right:16px">170</div><div data-line-number="171" class="react-line-number react-code-text" style="padding-right:16px">171</div><div data-line-number="172" class="react-line-number react-code-text" style="padding-right:16px">172</div><div data-line-number="173" class="react-line-number react-code-text" style="padding-right:16px">173</div><div data-line-number="174" class="react-line-number react-code-text" style="padding-right:16px">174</div><div data-line-number="175" class="react-line-number react-code-text" style="padding-right:16px">175</div><div data-line-number="176" class="react-line-number react-code-text" style="padding-right:16px">176</div><div data-line-number="177" class="react-line-number react-code-text" style="padding-right:16px">177</div><div data-line-number="178" class="react-line-number react-code-text" style="padding-right:16px">178</div><div data-line-number="179" class="react-line-number react-code-text" style="padding-right:16px">179</div><div data-line-number="180" class="react-line-number react-code-text" style="padding-right:16px">180</div></div><div class="react-code-lines"><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" style="position:relative"><span class="pl-s">&quot;&quot;&quot;1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.&quot;&quot;&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" style="position:relative"><span class="pl-s1">list_number</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" style="position:relative"><span class="pl-k">while</span> <span class="pl-c1">True</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" style="position:relative">    <span class="pl-s1">num</span><span class="pl-c1">=</span><span class="pl-en">int</span>(<span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese numeros, ingrese 0 para finalizar:<span class="pl-cce">\n</span>&#039;</span>))</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">!=</span><span class="pl-c1">0</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" style="position:relative">        <span class="pl-s1">list_number</span>.<span class="pl-en">append</span>(<span class="pl-s1">num</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" style="position:relative">        <span class="pl-k">break</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">list_number</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" style="position:relative"><span class="pl-s">&quot;&quot;&quot;2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.&quot;&quot;&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" style="position:relative"><span class="pl-s1">number</span><span class="pl-c1">=</span><span class="pl-en">int</span>(<span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese numero que quiera eliminar:<span class="pl-cce">\n</span>&#039;</span>))</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" style="position:relative"><span class="pl-k">if</span> <span class="pl-s1">number</span> <span class="pl-c1">in</span> <span class="pl-s1">list_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" style="position:relative">    <span class="pl-s1">list_number</span>.<span class="pl-en">remove</span>(<span class="pl-s1">number</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" style="position:relative"><span class="pl-k">else</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" style="position:relative">    <span class="pl-en">print</span>(<span class="pl-s">&#039;no hay coincidencias&#039;</span>)                </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">list_number</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" style="position:relative"><span class="pl-c">#3.	Imprimir la sumatoria de todos los números de la lista.</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" style="position:relative"><span class="pl-s1">suma</span><span class="pl-c1">=</span><span class="pl-c1">0</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">list_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" style="position:relative">    <span class="pl-s1">suma</span><span class="pl-c1">+=</span><span class="pl-s1">i</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s">f&#039;la suma es: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">suma</span><span class="pl-kos">}</span></span>&#039;</span>)    </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" style="position:relative"><span class="pl-c">#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" style="position:relative"><span class="pl-s1">other_number</span><span class="pl-c1">=</span><span class="pl-en">int</span>(<span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese un numero: &#039;</span>))</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" style="position:relative"><span class="pl-s1">other_lista</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">list_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">i</span><span class="pl-c1">&lt;</span><span class="pl-s1">other_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" style="position:relative">        <span class="pl-s1">other_lista</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">other_lista</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" style="position:relative">    <span class="pl-en">print</span>(<span class="pl-s1">i</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" style="position:relative"><span class="pl-c">#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" style="position:relative"><span class="pl-s1">listanueva</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" style="position:relative"><span class="pl-s1">tupla</span><span class="pl-c1">=</span>()</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">list_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" style="position:relative">    <span class="pl-s1">cont</span><span class="pl-c1">=</span><span class="pl-c1">0</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" style="position:relative">    <span class="pl-k">for</span> <span class="pl-s1">k</span> <span class="pl-c1">in</span> <span class="pl-s1">list_number</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" style="position:relative">        <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">==</span><span class="pl-s1">k</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" style="position:relative">            <span class="pl-s1">cont</span><span class="pl-c1">+=</span><span class="pl-c1">1</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" style="position:relative">            <span class="pl-s1">tupla</span><span class="pl-c1">=</span>(<span class="pl-s1">i</span>,<span class="pl-s1">cont</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" style="position:relative">    <span class="pl-s1">listanueva</span>.<span class="pl-en">append</span>(<span class="pl-s1">tupla</span>)   </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" style="position:relative"><span class="pl-s1">listaset</span><span class="pl-c1">=</span><span class="pl-en">set</span>(<span class="pl-s1">listanueva</span>)            </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">listaset</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" style="position:relative">    </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" style="position:relative"><span class="pl-c">#6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" style="position:relative"><span class="pl-s1">listanombresPrimaria</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" style="position:relative"><span class="pl-s1">listanombresSecundaria</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" style="position:relative"><span class="pl-k">while</span> <span class="pl-c1">True</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" style="position:relative">    <span class="pl-s1">nombresp</span><span class="pl-c1">=</span><span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese nombres de primaria, para finalizar ingrese X:<span class="pl-cce">\n</span>&#039;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">nombresp</span><span class="pl-c1">!=</span><span class="pl-s">&#039;x&#039;</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" style="position:relative">        <span class="pl-s1">listanombresPrimaria</span>.<span class="pl-en">append</span>(<span class="pl-s1">nombresp</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">nombresp</span><span class="pl-c1">==</span><span class="pl-s">&#039;x&#039;</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" style="position:relative">        <span class="pl-k">break</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" style="position:relative"><span class="pl-k">while</span> <span class="pl-c1">True</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" style="position:relative">    <span class="pl-s1">nombress</span><span class="pl-c1">=</span><span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese nombres de secundaria, para finalizar ingrese X:<span class="pl-cce">\n</span>&#039;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">nombress</span><span class="pl-c1">!=</span><span class="pl-s">&#039;x&#039;</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" style="position:relative">        <span class="pl-s1">listanombresSecundaria</span>.<span class="pl-en">append</span>(<span class="pl-s1">nombress</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">nombress</span><span class="pl-c1">==</span><span class="pl-s">&#039;x&#039;</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" style="position:relative">        <span class="pl-k">break</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" style="position:relative"><span class="pl-c">#a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.    </span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" style="position:relative"><span class="pl-s1">todoslosnombres</span><span class="pl-c1">=</span><span class="pl-s1">listanombresPrimaria</span><span class="pl-c1">+</span><span class="pl-s1">listanombresSecundaria</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" style="position:relative"><span class="pl-s1">nombressinrepetir</span><span class="pl-c1">=</span><span class="pl-en">set</span>(<span class="pl-s1">todoslosnombres</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">nombressinrepetir</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" style="position:relative"><span class="pl-c">#b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" style="position:relative"><span class="pl-s1">nombresrepetidos</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" style="position:relative"><span class="pl-s1">nombresnorepetidos</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">listanombresPrimaria</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" style="position:relative">    <span class="pl-k">for</span> <span class="pl-s1">k</span> <span class="pl-c1">in</span> <span class="pl-s1">listanombresSecundaria</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" style="position:relative">        <span class="pl-k">if</span> <span class="pl-s1">i</span><span class="pl-c1">==</span><span class="pl-s1">k</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" style="position:relative">            <span class="pl-s1">nombresrepetidos</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" style="position:relative">        <span class="pl-c">#c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" style="position:relative">        <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">listanombresSecundaria</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" style="position:relative">            <span class="pl-s1">nombresnorepetidos</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" style="position:relative"><span class="pl-s1">nombresrepetidos</span><span class="pl-c1">=</span><span class="pl-en">set</span>(<span class="pl-s1">nombresrepetidos</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" style="position:relative"><span class="pl-s1">nombresnorepetidos</span><span class="pl-c1">=</span><span class="pl-en">set</span>(<span class="pl-s1">nombresnorepetidos</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">nombresrepetidos</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">nombresnorepetidos</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" style="position:relative"><span class="pl-c">#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" style="position:relative"><span class="pl-c">#‘r’:5</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" style="position:relative"><span class="pl-c">#‘%’:3</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" style="position:relative"><span class="pl-c">#‘a’:8</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" style="position:relative"><span class="pl-c">#‘9’:1</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" style="position:relative"><span class="pl-s1">listastr</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" style="position:relative"><span class="pl-s1">contt</span><span class="pl-c1">=</span><span class="pl-c1">0</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" style="position:relative"><span class="pl-k">while</span> <span class="pl-c1">True</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" style="position:relative">    <span class="pl-s1">string</span><span class="pl-c1">=</span><span class="pl-en">input</span>(<span class="pl-s">&#039;ingrese una string: <span class="pl-cce">\n</span>&#039;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" style="position:relative">    <span class="pl-s1">listastr</span>.<span class="pl-en">append</span>(<span class="pl-s1">string</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" style="position:relative">    <span class="pl-s1">contt</span><span class="pl-c1">+=</span><span class="pl-c1">1</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">contt</span><span class="pl-c1">==</span><span class="pl-c1">50</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" style="position:relative">        <span class="pl-k">break</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" style="position:relative"><span class="pl-s1">listanuevastr</span><span class="pl-c1">=</span>[]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" style="position:relative"><span class="pl-s1">tuplastr</span><span class="pl-c1">=</span>()</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" style="position:relative"><span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">listastr</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" style="position:relative">    <span class="pl-s1">cont</span><span class="pl-c1">=</span><span class="pl-c1">0</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" style="position:relative">    <span class="pl-k">for</span> <span class="pl-s1">k</span> <span class="pl-c1">in</span> <span class="pl-s1">listastr</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" style="position:relative">        <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">==</span><span class="pl-s1">k</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" style="position:relative">            <span class="pl-s1">cont</span><span class="pl-c1">+=</span><span class="pl-c1">1</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" style="position:relative">            <span class="pl-s1">tuplastr</span><span class="pl-c1">=</span>(<span class="pl-s1">i</span>,<span class="pl-s1">cont</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" style="position:relative">    <span class="pl-s1">listanuevastr</span>.<span class="pl-en">append</span>(<span class="pl-s1">tuplastr</span>)   </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" style="position:relative"><span class="pl-s1">listaset</span><span class="pl-c1">=</span><span class="pl-en">set</span>(<span class="pl-s1">listanuevastr</span>)            </div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">listaset</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" style="position:relative"><span class="pl-c">#8 trabajo de los equipos de futbol</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">res</span>(<span class="pl-s1">matriz</span>, <span class="pl-s1">num</span>):</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" style="position:relative">    <span class="pl-s1">contvic</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" style="position:relative">    <span class="pl-s1">contderr</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" style="position:relative">    <span class="pl-s1">contemp</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" style="position:relative">    <span class="pl-s1">conpuntos</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" style="position:relative">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">matriz</span>)):</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" style="position:relative">        <span class="pl-k">for</span> <span class="pl-s1">j</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">matriz</span>)):</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" style="position:relative">            <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">!=</span> <span class="pl-s1">j</span>:</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" style="position:relative">                <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">==</span> <span class="pl-s1">num</span>:</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC119" class="react-file-line html-div" data-testid="code-cell" data-line-number="119" style="position:relative">                    <span class="pl-k">if</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">i</span>][<span class="pl-s1">j</span>] <span class="pl-c1">&lt;</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">j</span>][<span class="pl-s1">i</span>]:</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC120" class="react-file-line html-div" data-testid="code-cell" data-line-number="120" style="position:relative">                        <span class="pl-s1">contderr</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC121" class="react-file-line html-div" data-testid="code-cell" data-line-number="121" style="position:relative">                    <span class="pl-k">elif</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">i</span>][<span class="pl-s1">j</span>] <span class="pl-c1">&gt;</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">j</span>][<span class="pl-s1">i</span>]:</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC122" class="react-file-line html-div" data-testid="code-cell" data-line-number="122" style="position:relative">                        <span class="pl-s1">contvic</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC123" class="react-file-line html-div" data-testid="code-cell" data-line-number="123" style="position:relative">                        <span class="pl-s1">conpuntos</span> <span class="pl-c1">+=</span> <span class="pl-c1">3</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC124" class="react-file-line html-div" data-testid="code-cell" data-line-number="124" style="position:relative">                    <span class="pl-k">else</span>:</div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC125" class="react-file-line html-div" data-testid="code-cell" data-line-number="125" style="position:relative">                        <span class="pl-s1">conpuntos</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC126" class="react-file-line html-div" data-testid="code-cell" data-line-number="126" style="position:relative">                        <span class="pl-s1">contemp</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></div></div></div><div class="child-of-line-110  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC127" class="react-file-line html-div" data-testid="code-cell" data-line-number="127" style="position:relative">    <span class="pl-s1">listaestadisticas</span> <span class="pl-c1">=</span> [<span class="pl-s1">contvic</span>, <span class="pl-s1">contderr</span>, <span class="pl-s1">contemp</span>, <span class="pl-s1">conpuntos</span>]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC128" class="react-file-line html-div" data-testid="code-cell" data-line-number="128" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s1">listaestadisticas</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC129" class="react-file-line html-div" data-testid="code-cell" data-line-number="129" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC130" class="react-file-line html-div" data-testid="code-cell" data-line-number="130" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC131" class="react-file-line html-div" data-testid="code-cell" data-line-number="131" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">dif</span>(<span class="pl-s1">matriz</span>, <span class="pl-s1">num</span>):</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC132" class="react-file-line html-div" data-testid="code-cell" data-line-number="132" style="position:relative">    <span class="pl-s1">sum</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC133" class="react-file-line html-div" data-testid="code-cell" data-line-number="133" style="position:relative">    <span class="pl-s1">golesrecibidos</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC134" class="react-file-line html-div" data-testid="code-cell" data-line-number="134" style="position:relative">    <span class="pl-s1">cont</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC135" class="react-file-line html-div" data-testid="code-cell" data-line-number="135" style="position:relative">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">num</span>]:</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC136" class="react-file-line html-div" data-testid="code-cell" data-line-number="136" style="position:relative">        <span class="pl-s1">sum</span> <span class="pl-c1">+=</span> <span class="pl-s1">i</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC137" class="react-file-line html-div" data-testid="code-cell" data-line-number="137" style="position:relative">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">matriz</span>)):</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC138" class="react-file-line html-div" data-testid="code-cell" data-line-number="138" style="position:relative">            <span class="pl-k">for</span> <span class="pl-s1">j</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">matriz</span>)):</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC139" class="react-file-line html-div" data-testid="code-cell" data-line-number="139" style="position:relative">                <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">!=</span> <span class="pl-s1">j</span>:</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC140" class="react-file-line html-div" data-testid="code-cell" data-line-number="140" style="position:relative">                    <span class="pl-k">if</span> <span class="pl-s1">cont</span> <span class="pl-c1">==</span> <span class="pl-c1">3</span>:</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC141" class="react-file-line html-div" data-testid="code-cell" data-line-number="141" style="position:relative">                        <span class="pl-k">break</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC142" class="react-file-line html-div" data-testid="code-cell" data-line-number="142" style="position:relative">                    <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">==</span> <span class="pl-s1">num</span>:</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC143" class="react-file-line html-div" data-testid="code-cell" data-line-number="143" style="position:relative">                        <span class="pl-s1">golesrecibidos</span> <span class="pl-c1">+=</span> <span class="pl-s1">matriz</span>[<span class="pl-s1">j</span>][<span class="pl-s1">i</span>]</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC144" class="react-file-line html-div" data-testid="code-cell" data-line-number="144" style="position:relative">
</div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC145" class="react-file-line html-div" data-testid="code-cell" data-line-number="145" style="position:relative">                        <span class="pl-s1">cont</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC146" class="react-file-line html-div" data-testid="code-cell" data-line-number="146" style="position:relative">    <span class="pl-s1">res</span> <span class="pl-c1">=</span> <span class="pl-s1">sum</span> <span class="pl-c1">-</span> <span class="pl-s1">golesrecibidos</span></div></div></div><div class="child-of-line-131  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC147" class="react-file-line html-div" data-testid="code-cell" data-line-number="147" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC148" class="react-file-line html-div" data-testid="code-cell" data-line-number="148" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s">f&quot;equipo<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">num</span><span class="pl-c1">+</span><span class="pl-c1">1</span><span class="pl-kos">}</span></span> la diferencia es : <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">res</span><span class="pl-kos">}</span></span> &quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC149" class="react-file-line html-div" data-testid="code-cell" data-line-number="149" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC150" class="react-file-line html-div" data-testid="code-cell" data-line-number="150" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC151" class="react-file-line html-div" data-testid="code-cell" data-line-number="151" style="position:relative"><span class="pl-s1">matriz</span> <span class="pl-c1">=</span> [[<span class="pl-c1">0</span>, <span class="pl-c1">4</span>, <span class="pl-c1">2</span>, <span class="pl-c1">1</span>], [<span class="pl-c1">5</span>, <span class="pl-c1">0</span>, <span class="pl-c1">3</span>, <span class="pl-c1">2</span>], [<span class="pl-c1">0</span>, <span class="pl-c1">2</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>], [<span class="pl-c1">1</span>, <span class="pl-c1">0</span>, <span class="pl-c1">2</span>, <span class="pl-c1">0</span>]]</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC152" class="react-file-line html-div" data-testid="code-cell" data-line-number="152" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC153" class="react-file-line html-div" data-testid="code-cell" data-line-number="153" style="position:relative"><span class="pl-s1">estadisticasequipo1</span> <span class="pl-c1">=</span> <span class="pl-en">res</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">0</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC154" class="react-file-line html-div" data-testid="code-cell" data-line-number="154" style="position:relative"><span class="pl-en">print</span>(</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC155" class="react-file-line html-div" data-testid="code-cell" data-line-number="155" style="position:relative">    <span class="pl-s">f&quot;Equipo 1: Victorias=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo1</span>[<span class="pl-c1">0</span>]<span class="pl-kos">}</span></span>, Derrotas=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo1</span>[<span class="pl-c1">1</span>]<span class="pl-kos">}</span></span>, Empates=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo1</span>[<span class="pl-c1">2</span>]<span class="pl-kos">}</span></span>, puntosTotales= <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo1</span>[<span class="pl-c1">3</span>]<span class="pl-kos">}</span></span>&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC156" class="react-file-line html-div" data-testid="code-cell" data-line-number="156" style="position:relative">)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC157" class="react-file-line html-div" data-testid="code-cell" data-line-number="157" style="position:relative"><span class="pl-s1">dif1</span> <span class="pl-c1">=</span> <span class="pl-en">dif</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">0</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC158" class="react-file-line html-div" data-testid="code-cell" data-line-number="158" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">dif1</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC159" class="react-file-line html-div" data-testid="code-cell" data-line-number="159" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC160" class="react-file-line html-div" data-testid="code-cell" data-line-number="160" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC161" class="react-file-line html-div" data-testid="code-cell" data-line-number="161" style="position:relative"><span class="pl-s1">estadisticasequipo2</span> <span class="pl-c1">=</span> <span class="pl-en">res</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">1</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC162" class="react-file-line html-div" data-testid="code-cell" data-line-number="162" style="position:relative"><span class="pl-en">print</span>(</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC163" class="react-file-line html-div" data-testid="code-cell" data-line-number="163" style="position:relative">    <span class="pl-s">f&quot;Equipo 2: Victorias=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo2</span>[<span class="pl-c1">0</span>]<span class="pl-kos">}</span></span>, Derrotas=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo2</span>[<span class="pl-c1">1</span>]<span class="pl-kos">}</span></span>, Empates=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo2</span>[<span class="pl-c1">2</span>]<span class="pl-kos">}</span></span>,  puntosTotales= <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo2</span>[<span class="pl-c1">3</span>]<span class="pl-kos">}</span></span>&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC164" class="react-file-line html-div" data-testid="code-cell" data-line-number="164" style="position:relative">)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC165" class="react-file-line html-div" data-testid="code-cell" data-line-number="165" style="position:relative"><span class="pl-s1">dif2</span> <span class="pl-c1">=</span> <span class="pl-en">dif</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">1</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC166" class="react-file-line html-div" data-testid="code-cell" data-line-number="166" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">dif2</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC167" class="react-file-line html-div" data-testid="code-cell" data-line-number="167" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC168" class="react-file-line html-div" data-testid="code-cell" data-line-number="168" style="position:relative"><span class="pl-s1">estadisticasequipo3</span> <span class="pl-c1">=</span> <span class="pl-en">res</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">2</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC169" class="react-file-line html-div" data-testid="code-cell" data-line-number="169" style="position:relative"><span class="pl-en">print</span>(</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC170" class="react-file-line html-div" data-testid="code-cell" data-line-number="170" style="position:relative">    <span class="pl-s">f&quot;Equipo 3: Victorias=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo3</span>[<span class="pl-c1">0</span>]<span class="pl-kos">}</span></span>, Derrotas=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo3</span>[<span class="pl-c1">1</span>]<span class="pl-kos">}</span></span>, Empates=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo3</span>[<span class="pl-c1">2</span>]<span class="pl-kos">}</span></span>, puntosTotales= <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo3</span>[<span class="pl-c1">3</span>]<span class="pl-kos">}</span></span>&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC171" class="react-file-line html-div" data-testid="code-cell" data-line-number="171" style="position:relative">)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC172" class="react-file-line html-div" data-testid="code-cell" data-line-number="172" style="position:relative"><span class="pl-s1">dif3</span> <span class="pl-c1">=</span> <span class="pl-en">dif</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">2</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC173" class="react-file-line html-div" data-testid="code-cell" data-line-number="173" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">dif3</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC174" class="react-file-line html-div" data-testid="code-cell" data-line-number="174" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC175" class="react-file-line html-div" data-testid="code-cell" data-line-number="175" style="position:relative"><span class="pl-s1">estadisticasequipo4</span> <span class="pl-c1">=</span> <span class="pl-en">res</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">3</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC176" class="react-file-line html-div" data-testid="code-cell" data-line-number="176" style="position:relative"><span class="pl-en">print</span>(</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC177" class="react-file-line html-div" data-testid="code-cell" data-line-number="177" style="position:relative">    <span class="pl-s">f&quot;Equipo 4: Victorias=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo4</span>[<span class="pl-c1">0</span>]<span class="pl-kos">}</span></span>, Derrotas=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo4</span>[<span class="pl-c1">1</span>]<span class="pl-kos">}</span></span>, Empates=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo4</span>[<span class="pl-c1">2</span>]<span class="pl-kos">}</span></span>, puntosTotales= <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">estadisticasequipo4</span>[<span class="pl-c1">3</span>]<span class="pl-kos">}</span></span>&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC178" class="react-file-line html-div" data-testid="code-cell" data-line-number="178" style="position:relative">)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC179" class="react-file-line html-div" data-testid="code-cell" data-line-number="179" style="position:relative"><span class="pl-s1">dif4</span> <span class="pl-c1">=</span> <span class="pl-en">dif</span>(<span class="pl-s1">matriz</span>, <span class="pl-c1">3</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC180" class="react-file-line html-div" data-testid="code-cell" data-line-number="180" style="position:relative"><span class="pl-en">print</span>(<span class="pl-s1">dif4</span>)</div></div></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div><button hidden="" data-testid="hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></section></div></div><div class="Box-sc-g0xbh4-0 ktQnIo"></div><div class="Box-sc-g0xbh4-0 bgHcBP panel-content-narrow-styles inner-panel-content-not-narrow"><div id="symbols-pane" class="Box-sc-g0xbh4-0"><div aria-labelledby="symbols-pane-header" class="Box-sc-g0xbh4-0 bJNAmt"><div class="Box-sc-g0xbh4-0 ipXucK"><h2 id="symbols-pane-header" tabindex="-1" class="Box-sc-g0xbh4-0 wMEyi">Symbols</h2><button data-component="IconButton" type="button" aria-label="Close symbols" data-hotkey="Escape" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 gmlGme"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button></div><div class="Box-sc-g0xbh4-0 igdeeu">Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code.</div><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 hdWBGU kdlhpP TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M.75 3h14.5a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1 0-1.5ZM3 7.75A.75.75 0 0 1 3.75 7h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 7.75Zm3 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg></span><input type="text" placeholder="Filter symbols" name="Filter symbols" aria-label="Filter symbols" aria-controls="filter-results" aria-expanded="true" aria-autocomplete="list" role="combobox" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""/><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 ckwgci"><kbd>r</kbd></div></span></span><div class="Box-sc-g0xbh4-0 jGYebd"><div class="Box-sc-g0xbh4-0 kgNotW"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Code Navigation" data-omit-spacer="true" class="TreeView__UlBox-sc-4ex6b6-0 gtekST"><li class="PRIVATE_TreeView-item" tabindex="0" id="0list_number" role="treeitem" aria-labelledby=":R6hlqlajal5:" aria-describedby=":R6hlqlajal5H1: :R6hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="list_number" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">list_number</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="1number" role="treeitem" aria-labelledby=":Rahlqlajal5:" aria-describedby=":Rahlqlajal5H1: :Rahlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rahlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="number" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">number</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="2suma" role="treeitem" aria-labelledby=":Rehlqlajal5:" aria-describedby=":Rehlqlajal5H1: :Rehlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rehlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="suma" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">suma</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="3other_number" role="treeitem" aria-labelledby=":Rihlqlajal5:" aria-describedby=":Rihlqlajal5H1: :Rihlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rihlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="other_number" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">other_number</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="4other_lista" role="treeitem" aria-labelledby=":Rmhlqlajal5:" aria-describedby=":Rmhlqlajal5H1: :Rmhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rmhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="other_lista" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">other_lista</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="5listanueva" role="treeitem" aria-labelledby=":Rqhlqlajal5:" aria-describedby=":Rqhlqlajal5H1: :Rqhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rqhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listanueva" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listanueva</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="6tupla" role="treeitem" aria-labelledby=":Ruhlqlajal5:" aria-describedby=":Ruhlqlajal5H1: :Ruhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Ruhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="tupla" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">tupla</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="7listaset" role="treeitem" aria-labelledby=":R12hlqlajal5:" aria-describedby=":R12hlqlajal5H1: :R12hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R12hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listaset" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listaset</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="8listanombresPrimaria" role="treeitem" aria-labelledby=":R16hlqlajal5:" aria-describedby=":R16hlqlajal5H1: :R16hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R16hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listanombresPrimaria" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listanombresPrimaria</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="9listanombresSecundaria" role="treeitem" aria-labelledby=":R1ahlqlajal5:" aria-describedby=":R1ahlqlajal5H1: :R1ahlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1ahlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listanombresSecundaria" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listanombresSecundaria</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="10todoslosnombres" role="treeitem" aria-labelledby=":R1ehlqlajal5:" aria-describedby=":R1ehlqlajal5H1: :R1ehlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1ehlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="todoslosnombres" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">todoslosnombres</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="11nombressinrepetir" role="treeitem" aria-labelledby=":R1ihlqlajal5:" aria-describedby=":R1ihlqlajal5H1: :R1ihlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1ihlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="nombressinrepetir" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">nombressinrepetir</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="12nombresrepetidos" role="treeitem" aria-labelledby=":R1mhlqlajal5:" aria-describedby=":R1mhlqlajal5H1: :R1mhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1mhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="nombresrepetidos" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">nombresrepetidos</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="13nombresnorepetidos" role="treeitem" aria-labelledby=":R1qhlqlajal5:" aria-describedby=":R1qhlqlajal5H1: :R1qhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1qhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="nombresnorepetidos" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">nombresnorepetidos</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="14nombresrepetidos" role="treeitem" aria-labelledby=":R1uhlqlajal5:" aria-describedby=":R1uhlqlajal5H1: :R1uhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1uhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="nombresrepetidos" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">nombresrepetidos</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="15nombresnorepetidos" role="treeitem" aria-labelledby=":R22hlqlajal5:" aria-describedby=":R22hlqlajal5H1: :R22hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R22hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="nombresnorepetidos" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">nombresnorepetidos</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="16listastr" role="treeitem" aria-labelledby=":R26hlqlajal5:" aria-describedby=":R26hlqlajal5H1: :R26hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R26hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listastr" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listastr</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="17contt" role="treeitem" aria-labelledby=":R2ahlqlajal5:" aria-describedby=":R2ahlqlajal5H1: :R2ahlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2ahlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="contt" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">contt</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="18listanuevastr" role="treeitem" aria-labelledby=":R2ehlqlajal5:" aria-describedby=":R2ehlqlajal5H1: :R2ehlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2ehlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listanuevastr" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listanuevastr</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="19tuplastr" role="treeitem" aria-labelledby=":R2ihlqlajal5:" aria-describedby=":R2ihlqlajal5H1: :R2ihlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2ihlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="tuplastr" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">tuplastr</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="20listaset" role="treeitem" aria-labelledby=":R2mhlqlajal5:" aria-describedby=":R2mhlqlajal5H1: :R2mhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2mhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="listaset" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">listaset</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="21res" role="treeitem" aria-labelledby=":R2qhlqlajal5:" aria-describedby=":R2qhlqlajal5H1: :R2qhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2qhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 gJbnxT"></div><div class="Box-sc-g0xbh4-0 cwQfpp">func</div></div>  <div title="res" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">res</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="22dif" role="treeitem" aria-labelledby=":R2uhlqlajal5:" aria-describedby=":R2uhlqlajal5H1: :R2uhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2uhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 gJbnxT"></div><div class="Box-sc-g0xbh4-0 cwQfpp">func</div></div>  <div title="dif" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">dif</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="23matriz" role="treeitem" aria-labelledby=":R32hlqlajal5:" aria-describedby=":R32hlqlajal5H1: :R32hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R32hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="matriz" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">matriz</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="24estadisticasequipo1" role="treeitem" aria-labelledby=":R36hlqlajal5:" aria-describedby=":R36hlqlajal5H1: :R36hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R36hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="estadisticasequipo1" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">estadisticasequipo1</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="25dif1" role="treeitem" aria-labelledby=":R3ahlqlajal5:" aria-describedby=":R3ahlqlajal5H1: :R3ahlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3ahlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="dif1" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">dif1</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="26estadisticasequipo2" role="treeitem" aria-labelledby=":R3ehlqlajal5:" aria-describedby=":R3ehlqlajal5H1: :R3ehlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3ehlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="estadisticasequipo2" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">estadisticasequipo2</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="27dif2" role="treeitem" aria-labelledby=":R3ihlqlajal5:" aria-describedby=":R3ihlqlajal5H1: :R3ihlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3ihlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="dif2" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">dif2</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="28estadisticasequipo3" role="treeitem" aria-labelledby=":R3mhlqlajal5:" aria-describedby=":R3mhlqlajal5H1: :R3mhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3mhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="estadisticasequipo3" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">estadisticasequipo3</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="29dif3" role="treeitem" aria-labelledby=":R3qhlqlajal5:" aria-describedby=":R3qhlqlajal5H1: :R3qhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3qhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="dif3" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">dif3</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="30estadisticasequipo4" role="treeitem" aria-labelledby=":R3uhlqlajal5:" aria-describedby=":R3uhlqlajal5H1: :R3uhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3uhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="estadisticasequipo4" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">estadisticasequipo4</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="31dif4" role="treeitem" aria-labelledby=":R42hlqlajal5:" aria-describedby=":R42hlqlajal5H1: :R42hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R42hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 fQgtqx"></div><div class="Box-sc-g0xbh4-0 EVPPH">const</div></div>  <div title="dif4" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">dif4</span></div></div></span></div></div></li></ul></div></div></div></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></main></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></div> <!-- --> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"day"}</script></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive" role="contentinfo">
  <h2 class='sr-only'>Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>        <span>
        &copy; 2023 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label='Footer' class="col-12 col-lg-8">
      <h3 class='sr-only' id='sr-footer-heading'>Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby='sr-footer-heading'>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>


    <style>
      .user-mention[href$="/SebastianASU2005"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" ></div>
  </body>
</html>

