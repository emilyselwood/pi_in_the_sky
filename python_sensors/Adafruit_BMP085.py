




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>Adafruit-Raspberry-Pi-Python-Code/Adafruit_BMP085/Adafruit_BMP085.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code · GitHub</title>
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

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="B91E0808:5BB6:9FBF12:53AED0AA" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="te/wEKtb7KJvoqa/pdS119xocQQcrTtR/QuoXiqenBNSCl6395A8Y6lmiTTRUclBQWf7+g6JhIgvW/YwEgq47Q==" name="csrf-token" />

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
      <a class="button signin" href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code%2Fblob%2Fmaster%2FAdafruit_BMP085%2FAdafruit_BMP085.py">Sign in</a>
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
          


<a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/c090f6bc47452050bc4b1369e7a4dbf7a9f68993/Adafruit_BMP085/Adafruit_BMP085.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:cf1a1fe58567b09395040b2cdd04fa0a -->

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
              <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_BMP085/Adafruit_BMP085.py"
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
          data-clipboard-text="Adafruit_BMP085/Adafruit_BMP085.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Adafruit-Raspberry-Pi-Python-Code</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_BMP085" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Adafruit_BMP085</span></a></span><span class="separator"> / </span><strong class="final-path">Adafruit_BMP085.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="" class="main-avatar" height="24" src="https://2.gravatar.com/avatar/daa9b954b88210084e3687db33644adb?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=x&amp;s=140" width="24" />
      <span class="author"><span>KTOWN</span></span>
      <time datetime="2013-09-02T21:12:45+02:00" is="relative-time">September 02, 2013</time>
      <div class="commit-title">
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commit/7e950cf19bc5ca7ba511dcc22e960fe4c7ec3b91" class="message" data-pjax="true" title="Updated 16 bit reads to local functions">Updated 16 bit reads to local functions</a>
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
          <span>260 lines (229 sloc)</span>
          <span class="meta-divider"></span>
        <span>8.231 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/raw/master/Adafruit_BMP085/Adafruit_BMP085.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blame/master/Adafruit_BMP085/Adafruit_BMP085.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_BMP085/Adafruit_BMP085.py" class="minibutton " rel="nofollow">History</a>
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
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">Adafruit_I2C</span> <span class="kn">import</span> <span class="n">Adafruit_I2C</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="c"># ===========================================================================</span></div><div class='line' id='LC7'><span class="c"># BMP085 Class</span></div><div class='line' id='LC8'><span class="c"># ===========================================================================</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="k">class</span> <span class="nc">BMP085</span> <span class="p">:</span></div><div class='line' id='LC11'>&nbsp;&nbsp;<span class="n">i2c</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'>&nbsp;&nbsp;<span class="c"># Operating Modes</span></div><div class='line' id='LC14'>&nbsp;&nbsp;<span class="n">__BMP085_ULTRALOWPOWER</span>     <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC15'>&nbsp;&nbsp;<span class="n">__BMP085_STANDARD</span>          <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC16'>&nbsp;&nbsp;<span class="n">__BMP085_HIGHRES</span>           <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC17'>&nbsp;&nbsp;<span class="n">__BMP085_ULTRAHIGHRES</span>      <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'>&nbsp;&nbsp;<span class="c"># BMP085 Registers</span></div><div class='line' id='LC20'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC1</span>           <span class="o">=</span> <span class="mh">0xAA</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC21'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC2</span>           <span class="o">=</span> <span class="mh">0xAC</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC22'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC3</span>           <span class="o">=</span> <span class="mh">0xAE</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC23'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC4</span>           <span class="o">=</span> <span class="mh">0xB0</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC24'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC5</span>           <span class="o">=</span> <span class="mh">0xB2</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC25'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_AC6</span>           <span class="o">=</span> <span class="mh">0xB4</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC26'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_B1</span>            <span class="o">=</span> <span class="mh">0xB6</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC27'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_B2</span>            <span class="o">=</span> <span class="mh">0xB8</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC28'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_MB</span>            <span class="o">=</span> <span class="mh">0xBA</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_MC</span>            <span class="o">=</span> <span class="mh">0xBC</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC30'>&nbsp;&nbsp;<span class="n">__BMP085_CAL_MD</span>            <span class="o">=</span> <span class="mh">0xBE</span>  <span class="c"># R   Calibration data (16 bits)</span></div><div class='line' id='LC31'>&nbsp;&nbsp;<span class="n">__BMP085_CONTROL</span>           <span class="o">=</span> <span class="mh">0xF4</span></div><div class='line' id='LC32'>&nbsp;&nbsp;<span class="n">__BMP085_TEMPDATA</span>          <span class="o">=</span> <span class="mh">0xF6</span></div><div class='line' id='LC33'>&nbsp;&nbsp;<span class="n">__BMP085_PRESSUREDATA</span>      <span class="o">=</span> <span class="mh">0xF6</span></div><div class='line' id='LC34'>&nbsp;&nbsp;<span class="n">__BMP085_READTEMPCMD</span>       <span class="o">=</span> <span class="mh">0x2E</span></div><div class='line' id='LC35'>&nbsp;&nbsp;<span class="n">__BMP085_READPRESSURECMD</span>   <span class="o">=</span> <span class="mh">0x34</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'>&nbsp;&nbsp;<span class="c"># Private Fields</span></div><div class='line' id='LC38'>&nbsp;&nbsp;<span class="n">_cal_AC1</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC39'>&nbsp;&nbsp;<span class="n">_cal_AC2</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC40'>&nbsp;&nbsp;<span class="n">_cal_AC3</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC41'>&nbsp;&nbsp;<span class="n">_cal_AC4</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC42'>&nbsp;&nbsp;<span class="n">_cal_AC5</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC43'>&nbsp;&nbsp;<span class="n">_cal_AC6</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC44'>&nbsp;&nbsp;<span class="n">_cal_B1</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC45'>&nbsp;&nbsp;<span class="n">_cal_B2</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC46'>&nbsp;&nbsp;<span class="n">_cal_MB</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC47'>&nbsp;&nbsp;<span class="n">_cal_MC</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC48'>&nbsp;&nbsp;<span class="n">_cal_MD</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'>&nbsp;&nbsp;<span class="c"># Constructor</span></div><div class='line' id='LC51'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">address</span><span class="o">=</span><span class="mh">0x77</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">i2c</span> <span class="o">=</span> <span class="n">Adafruit_I2C</span><span class="p">(</span><span class="n">address</span><span class="p">)</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">address</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">debug</span> <span class="o">=</span> <span class="n">debug</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Make sure the specified mode is in the appropriate range</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">((</span><span class="n">mode</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">)</span> <span class="o">|</span> <span class="p">(</span><span class="n">mode</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">)):</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Invalid Mode: Using STANDARD by default&quot;</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_STANDARD</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">=</span> <span class="n">mode</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read the calibration data</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">readCalibrationData</span><span class="p">()</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readS16</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">register</span><span class="p">):</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Reads a signed 16-bit value&quot;</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hi</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readS8</span><span class="p">(</span><span class="n">register</span><span class="p">)</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="n">register</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="n">hi</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">lo</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readU16</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">register</span><span class="p">):</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Reads an unsigned 16-bit value&quot;</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hi</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="n">register</span><span class="p">)</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="n">register</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="n">hi</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">lo</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readCalibrationData</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Reads the calibration data from the IC&quot;</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC1</span><span class="p">)</span>   <span class="c"># INT16</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC2</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC2</span><span class="p">)</span>   <span class="c"># INT16</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC3</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC3</span><span class="p">)</span>   <span class="c"># INT16</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC4</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readU16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC4</span><span class="p">)</span>   <span class="c"># UINT16</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC5</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readU16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC5</span><span class="p">)</span>   <span class="c"># UINT16</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC6</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readU16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_AC6</span><span class="p">)</span>   <span class="c"># UINT16</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_B1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_B1</span><span class="p">)</span>     <span class="c"># INT16</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_B2</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_B2</span><span class="p">)</span>     <span class="c"># INT16</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MB</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_MB</span><span class="p">)</span>     <span class="c"># INT16</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MC</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_MC</span><span class="p">)</span>     <span class="c"># INT16</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MD</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readS16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CAL_MD</span><span class="p">)</span>     <span class="c"># INT16</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">showCalibrationData</span><span class="p">()</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">showCalibrationData</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Displays the calibration values for debugging purposes&quot;</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC1 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC1</span><span class="p">)</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC2 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC2</span><span class="p">)</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC3 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC3</span><span class="p">)</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC4 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC4</span><span class="p">)</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC5 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC5</span><span class="p">)</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: AC6 = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC6</span><span class="p">)</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B1  = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_B1</span><span class="p">)</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B2  = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_B2</span><span class="p">)</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: MB  = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_MB</span><span class="p">)</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: MC  = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_MC</span><span class="p">)</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: MD  = </span><span class="si">%6d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_MD</span><span class="p">)</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readRawTemp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Reads the raw (uncompensated) temperature from the sensor&quot;</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">write8</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CONTROL</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_READTEMPCMD</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.005</span><span class="p">)</span>  <span class="c"># Wait 5ms</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">raw</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readU16</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_TEMPDATA</span><span class="p">)</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: Raw Temp: 0x</span><span class="si">%04X</span><span class="s"> (</span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">raw</span> <span class="o">&amp;</span> <span class="mh">0xFFFF</span><span class="p">,</span> <span class="n">raw</span><span class="p">)</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">raw</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readRawPressure</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Reads the raw (uncompensated) pressure level from the sensor&quot;</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">write8</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_CONTROL</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_READPRESSURECMD</span> <span class="o">+</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">&lt;&lt;</span> <span class="mi">6</span><span class="p">))</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_ULTRALOWPOWER</span><span class="p">):</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.005</span><span class="p">)</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_HIGHRES</span><span class="p">):</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.014</span><span class="p">)</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_ULTRAHIGHRES</span><span class="p">):</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.026</span><span class="p">)</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.008</span><span class="p">)</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msb</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_PRESSUREDATA</span><span class="p">)</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lsb</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_PRESSUREDATA</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xlsb</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">i2c</span><span class="o">.</span><span class="n">readU8</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_PRESSUREDATA</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">raw</span> <span class="o">=</span> <span class="p">((</span><span class="n">msb</span> <span class="o">&lt;&lt;</span> <span class="mi">16</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">lsb</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">xlsb</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="p">(</span><span class="mi">8</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span><span class="p">)</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: Raw Pressure: 0x</span><span class="si">%04X</span><span class="s"> (</span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">raw</span> <span class="o">&amp;</span> <span class="mh">0xFFFF</span><span class="p">,</span> <span class="n">raw</span><span class="p">)</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">raw</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readTemperature</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Gets the compensated temperature in degrees celcius&quot;</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UT</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B5</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">temp</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read raw temp before aligning it with the calibration values</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UT</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readRawTemp</span><span class="p">()</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">((</span><span class="n">UT</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC6</span><span class="p">)</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC5</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">15</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_MC</span> <span class="o">&lt;&lt;</span> <span class="mi">11</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="n">X1</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_MD</span><span class="p">)</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B5</span> <span class="o">=</span> <span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">temp</span> <span class="o">=</span> <span class="p">((</span><span class="n">B5</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">4</span><span class="p">)</span> <span class="o">/</span> <span class="mf">10.0</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: Calibrated temperature = </span><span class="si">%f</span><span class="s"> C&quot;</span> <span class="o">%</span> <span class="n">temp</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">temp</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readPressure</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Gets the compensated pressure in pascal&quot;</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UT</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UP</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B3</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B5</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B6</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X3</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B4</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B7</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UT</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readRawTemp</span><span class="p">()</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UP</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readRawPressure</span><span class="p">()</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># You can use the datasheet values to test the conversion results</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># dsValues = True</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dsValues</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">dsValues</span><span class="p">):</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UT</span> <span class="o">=</span> <span class="mi">27898</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">UP</span> <span class="o">=</span> <span class="mi">23843</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC6</span> <span class="o">=</span> <span class="mi">23153</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC5</span> <span class="o">=</span> <span class="mi">32757</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MB</span> <span class="o">=</span> <span class="o">-</span><span class="mi">32768</span><span class="p">;</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MC</span> <span class="o">=</span> <span class="o">-</span><span class="mi">8711</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_MD</span> <span class="o">=</span> <span class="mi">2868</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_B1</span> <span class="o">=</span> <span class="mi">6190</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_B2</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC3</span> <span class="o">=</span> <span class="o">-</span><span class="mi">14383</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC2</span> <span class="o">=</span> <span class="o">-</span><span class="mi">72</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC1</span> <span class="o">=</span> <span class="mi">408</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC4</span> <span class="o">=</span> <span class="mi">32741</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__BMP085_ULTRALOWPOWER</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">showCalibrationData</span><span class="p">()</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># True Temperature Calculations</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">((</span><span class="n">UT</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC6</span><span class="p">)</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC5</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">15</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_MC</span> <span class="o">&lt;&lt;</span> <span class="mi">11</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="n">X1</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cal_MD</span><span class="p">)</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B5</span> <span class="o">=</span> <span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X1 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X1</span><span class="p">)</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X2 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X2</span><span class="p">)</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B5 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">B5</span><span class="p">)</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: True Temperature = </span><span class="si">%.2f</span><span class="s"> C&quot;</span> <span class="o">%</span> <span class="p">(((</span><span class="n">B5</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">4</span><span class="p">)</span> <span class="o">/</span> <span class="mf">10.0</span><span class="p">)</span></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Pressure Calculations</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B6</span> <span class="o">=</span> <span class="n">B5</span> <span class="o">-</span> <span class="mi">4000</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_B2</span> <span class="o">*</span> <span class="p">(</span><span class="n">B6</span> <span class="o">*</span> <span class="n">B6</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">12</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">11</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC2</span> <span class="o">*</span> <span class="n">B6</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">11</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X3</span> <span class="o">=</span> <span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B3</span> <span class="o">=</span> <span class="p">(((</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC1</span> <span class="o">*</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">X3</span><span class="p">)</span> <span class="o">&lt;&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span><span class="p">)</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B6 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">B6</span><span class="p">)</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X1 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X1</span><span class="p">)</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X2 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X2</span><span class="p">)</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X3 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X3</span><span class="p">)</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B3 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">B3</span><span class="p">)</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC3</span> <span class="o">*</span> <span class="n">B6</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">13</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_B1</span> <span class="o">*</span> <span class="p">((</span><span class="n">B6</span> <span class="o">*</span> <span class="n">B6</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">12</span><span class="p">))</span> <span class="o">&gt;&gt;</span> <span class="mi">16</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X3</span> <span class="o">=</span> <span class="p">((</span><span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span><span class="p">)</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">2</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B4</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cal_AC4</span> <span class="o">*</span> <span class="p">(</span><span class="n">X3</span> <span class="o">+</span> <span class="mi">32768</span><span class="p">))</span> <span class="o">&gt;&gt;</span> <span class="mi">15</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B7</span> <span class="o">=</span> <span class="p">(</span><span class="n">UP</span> <span class="o">-</span> <span class="n">B3</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="mi">50000</span> <span class="o">&gt;&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span><span class="p">)</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X1 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X1</span><span class="p">)</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X2 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X2</span><span class="p">)</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X3 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X3</span><span class="p">)</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B4 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">B4</span><span class="p">)</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: B7 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">B7</span><span class="p">)</span></div><div class='line' id='LC227'><br/></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">B7</span> <span class="o">&lt;</span> <span class="mh">0x80000000</span><span class="p">):</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="p">(</span><span class="n">B7</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="n">B4</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="p">(</span><span class="n">B7</span> <span class="o">/</span> <span class="n">B4</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X1 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X1</span><span class="p">)</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">(</span><span class="n">p</span> <span class="o">&gt;&gt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="n">p</span> <span class="o">&gt;&gt;</span> <span class="mi">8</span><span class="p">)</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X1</span> <span class="o">=</span> <span class="p">(</span><span class="n">X1</span> <span class="o">*</span> <span class="mi">3038</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">16</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">X2</span> <span class="o">=</span> <span class="p">(</span><span class="o">-</span><span class="mi">7357</span> <span class="o">*</span> <span class="n">p</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">16</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: p  = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X1 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X1</span><span class="p">)</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: X2 = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">X2</span><span class="p">)</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">p</span> <span class="o">+</span> <span class="p">((</span><span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span> <span class="o">+</span> <span class="mi">3791</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">4</span><span class="p">)</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: Pressure = </span><span class="si">%d</span><span class="s"> Pa&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC247'><br/></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">p</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">readAltitude</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">seaLevelPressure</span><span class="o">=</span><span class="mi">101325</span><span class="p">):</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Calculates the altitude in meters&quot;</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">altitude</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pressure</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readPressure</span><span class="p">())</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">altitude</span> <span class="o">=</span> <span class="mf">44330.0</span> <span class="o">*</span> <span class="p">(</span><span class="mf">1.0</span> <span class="o">-</span> <span class="nb">pow</span><span class="p">(</span><span class="n">pressure</span> <span class="o">/</span> <span class="n">seaLevelPressure</span><span class="p">,</span> <span class="mf">0.1903</span><span class="p">))</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">):</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;DBG: Altitude = </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">altitude</span><span class="p">)</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">altitude</span></div><div class='line' id='LC258'><br/></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">0</span></div></pre></div></td>
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
      <li>&copy; 2014 <span title="0.03432s from github-fe120-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
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

