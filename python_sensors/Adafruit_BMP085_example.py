




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>Adafruit-Raspberry-Pi-Python-Code/Adafruit_BMP085/Adafruit_BMP085_example.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" name="twitter:title" /><meta content="Adafruit-Raspberry-Pi-Python-Code - Adafruit library code for Raspberry Pi" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/181069?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/181069?s=400" property="og:image" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" property="og:title" /><meta content="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code" property="og:url" /><meta content="Adafruit-Raspberry-Pi-Python-Code - Adafruit library code for Raspberry Pi" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="B91E0808:5BB9:1E389CB:53AED0D1" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="QgWP2ELwwnv5uHf/Gln40lodFR80OIzXZOeORaQtXP9aJu+2cLLjKlhSpOzHgB6fb/dxXH9XHu+L5OrdI+sxEg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-bbf4e7b5ed0367744288dcb496d8dcb1b048f4a2.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-830b6eccd2ef85b203e66317cf87f0e48fa5f878.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="0b77784be2b2385480f4dba2d7968d09">

      
  <meta name="description" content="Adafruit-Raspberry-Pi-Python-Code - Adafruit library code for Raspberry Pi" />


  <meta content="181069" name="octolytics-dimension-user_id" /><meta content="adafruit" name="octolytics-dimension-user_login" /><meta content="5383151" name="octolytics-dimension-repository_id" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="5383151" name="octolytics-dimension-repository_network_root_id" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master.atom" rel="alternate" title="Recent Commits to Adafruit-Raspberry-Pi-Python-Code:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code%2Fblob%2Fmaster%2FAdafruit_BMP085%2FAdafruit_BMP085_example.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
          <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="adafruit/Adafruit-Raspberry-Pi-Python-Code"
      data-branch="master"
      data-sha="5f953b1422d0e4522be70a34659cba3fe5bb5275"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="adafruit/Adafruit-Raspberry-Pi-Python-Code" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
      <a href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/stargazers">
      512
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" class="social-count">
        320
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/adafruit" class="url fn" itemprop="url" rel="author"><span itemprop="title">adafruit</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-current-repository js-repo-home-link">Adafruit-Raspberry-Pi-Python-Code</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /adafruit/Adafruit-Raspberry-Pi-Python-Code">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /adafruit/Adafruit-Raspberry-Pi-Python-Code/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>19</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /adafruit/Adafruit-Raspberry-Pi-Python-Code/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>12</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /adafruit/Adafruit-Raspberry-Pi-Python-Code/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /adafruit/Adafruit-Raspberry-Pi-Python-Code/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /adafruit/Adafruit-Raspberry-Pi-Python-Code/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download adafruit/Adafruit-Raspberry-Pi-Python-Code as a zip file"
                   title="Download adafruit/Adafruit-Raspberry-Pi-Python-Code as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/c090f6bc47452050bc4b1369e7a4dbf7a9f68993/Adafruit_BMP085/Adafruit_BMP085_example.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:96cad678188378c0195be0a1582d596e -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_BMP085/Adafruit_BMP085_example.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="Adafruit_BMP085/Adafruit_BMP085_example.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Adafruit-Raspberry-Pi-Python-Code</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_BMP085" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Adafruit_BMP085</span></a></span><span class="separator"> / </span><strong class="final-path">Adafruit_BMP085_example.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="" class="main-avatar" height="24" src="https://2.gravatar.com/avatar/daa9b954b88210084e3687db33644adb?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=x&amp;s=140" width="24" />
      <span class="author"><span>KTOWN</span></span>
      <time datetime="2013-08-19T18:46:40+02:00" is="relative-time">August 19, 2013</time>
      <div class="commit-title">
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commit/457b4d0ff8e0f928b95fa6d48e77e81aa97752cb" class="message" data-pjax="true" title="More accurate altitude calculations">More accurate altitude calculations</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>0</strong>  contributors</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
        <span class="meta-divider"></span>
          <span>36 lines (26 sloc)</span>
          <span class="meta-divider"></span>
        <span>1.252 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/raw/master/Adafruit_BMP085/Adafruit_BMP085_example.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blame/master/Adafruit_BMP085/Adafruit_BMP085_example.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_BMP085/Adafruit_BMP085_example.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">Adafruit_BMP085</span> <span class="kn">import</span> <span class="n">BMP085</span></div><div class='line' id='LC4'><br/></div><div class='line' id='LC5'><span class="c"># ===========================================================================</span></div><div class='line' id='LC6'><span class="c"># Example Code</span></div><div class='line' id='LC7'><span class="c"># ===========================================================================</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="c"># Initialise the BMP085 and use STANDARD mode (default value)</span></div><div class='line' id='LC10'><span class="c"># bmp = BMP085(0x77, debug=True)</span></div><div class='line' id='LC11'><span class="n">bmp</span> <span class="o">=</span> <span class="n">BMP085</span><span class="p">(</span><span class="mh">0x77</span><span class="p">)</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="c"># To specify a different operating mode, uncomment one of the following:</span></div><div class='line' id='LC14'><span class="c"># bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode</span></div><div class='line' id='LC15'><span class="c"># bmp = BMP085(0x77, 1)  # STANDARD Mode</span></div><div class='line' id='LC16'><span class="c"># bmp = BMP085(0x77, 2)  # HIRES Mode</span></div><div class='line' id='LC17'><span class="c"># bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="n">temp</span> <span class="o">=</span> <span class="n">bmp</span><span class="o">.</span><span class="n">readTemperature</span><span class="p">()</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="c"># Read the current barometric pressure level</span></div><div class='line' id='LC22'><span class="n">pressure</span> <span class="o">=</span> <span class="n">bmp</span><span class="o">.</span><span class="n">readPressure</span><span class="p">()</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="c"># To calculate altitude based on an estimated mean sea level pressure</span></div><div class='line' id='LC25'><span class="c"># (1013.25 hPa) call the function as follows, but this won&#39;t be very accurate</span></div><div class='line' id='LC26'><span class="n">altitude</span> <span class="o">=</span> <span class="n">bmp</span><span class="o">.</span><span class="n">readAltitude</span><span class="p">()</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="c"># To specify a more accurate altitude, enter the correct mean sea level</span></div><div class='line' id='LC29'><span class="c"># pressure level.  For example, if the current pressure level is 1023.50 hPa</span></div><div class='line' id='LC30'><span class="c"># enter 102350 since we include two decimal places in the integer value</span></div><div class='line' id='LC31'><span class="c"># altitude = bmp.readAltitude(102350)</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="k">print</span> <span class="s">&quot;Temperature: </span><span class="si">%.2f</span><span class="s"> C&quot;</span> <span class="o">%</span> <span class="n">temp</span></div><div class='line' id='LC34'><span class="k">print</span> <span class="s">&quot;Pressure:    </span><span class="si">%.2f</span><span class="s"> hPa&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">pressure</span> <span class="o">/</span> <span class="mf">100.0</span><span class="p">)</span></div><div class='line' id='LC35'><span class="k">print</span> <span class="s">&quot;Altitude:    </span><span class="si">%.2f</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">altitude</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.02643s from github-fe128-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-90c3c3197777a26c93f4c80872dac101732fcb00.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-0f06d0f46fe7bcfbf31f2380f23aec15ba21b8ec.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

