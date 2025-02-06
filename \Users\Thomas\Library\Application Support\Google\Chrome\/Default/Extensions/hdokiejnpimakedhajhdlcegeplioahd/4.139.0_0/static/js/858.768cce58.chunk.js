"use strict";(self.webpackChunkwebClient=self.webpackChunkwebClient||[]).push([[858],{27858:(e,t,s)=>{s.r(t),s.d(t,{calculatePasswordStrength:()=>ae});const n=(e,t)=>e.push.apply(e,t),r=(e,t)=>e.split("").map((e=>t[e]||e)).join(""),a=e=>e.sort(((e,t)=>e.i-t.i||e.j-t.j)),o=e=>{const t={};let s=1;return e.forEach((e=>{t[e]=s,s+=1})),t};const i={4:[[1,2],[2,3]],5:[[1,3],[2,3],[2,4]],6:[[1,2],[2,4],[4,5]],7:[[1,3],[2,3],[4,5],[4,6]],8:[[2,4],[4,6]]},c=/^[A-Z\xbf-\xdf][^A-Z\xbf-\xdf]+$/,l=/^[^A-Z\xbf-\xdf]+[A-Z\xbf-\xdf]$/,h=/^[A-Z\xbf-\xdf]+$/,u=/^[^a-z\xdf-\xff]+$/,d=/^[a-z\xdf-\xff]+$/,g=/^[^A-Z\xbf-\xdf]+$/,p=/[a-z\xdf-\xff]/,f=/[A-Z\xbf-\xdf]/,m=/[^A-Za-z\xbf-\xdf]/gi,b=/^\d+$/,y=(new Date).getFullYear(),k={recentYear:/19\d\d|200\d|201\d|202\d/g};class w{match(e){let{password:t}=e;const s=[...this.getMatchesWithoutSeparator(t),...this.getMatchesWithSeparator(t)],n=this.filterNoise(s);return a(n)}getMatchesWithSeparator(e){const t=[],s=/^(\d{1,4})([\s/\\_.-])(\d{1,2})\2(\d{1,4})$/;for(let n=0;n<=Math.abs(e.length-6);n+=1)for(let r=n+5;r<=n+9&&!(r>=e.length);r+=1){const a=e.slice(n,+r+1||9e9),o=s.exec(a);if(null!=o){const e=this.mapIntegersToDayMonthYear([parseInt(o[1],10),parseInt(o[3],10),parseInt(o[4],10)]);null!=e&&t.push({pattern:"date",token:a,i:n,j:r,separator:o[2],year:e.year,month:e.month,day:e.day})}}return t}getMatchesWithoutSeparator(e){const t=[],s=/^\d{4,8}$/,n=e=>Math.abs(e.year-y);for(let r=0;r<=Math.abs(e.length-4);r+=1)for(let a=r+3;a<=r+7&&!(a>=e.length);a+=1){const o=e.slice(r,+a+1||9e9);if(s.exec(o)){const e=[],s=o.length;if(i[s].forEach((t=>{let[s,n]=t;const r=this.mapIntegersToDayMonthYear([parseInt(o.slice(0,s),10),parseInt(o.slice(s,n),10),parseInt(o.slice(n),10)]);null!=r&&e.push(r)})),e.length>0){let s=e[0],i=n(e[0]);e.slice(1).forEach((e=>{const t=n(e);t<i&&(s=e,i=t)})),t.push({pattern:"date",token:o,i:r,j:a,separator:"",year:s.year,month:s.month,day:s.day})}}}return t}filterNoise(e){return e.filter((t=>{let s=!1;const n=e.length;for(let r=0;r<n;r+=1){const n=e[r];if(t!==n&&n.i<=t.i&&n.j>=t.j){s=!0;break}}return!s}))}mapIntegersToDayMonthYear(e){if(e[1]>31||e[1]<=0)return null;let t=0,s=0,n=0;for(let r=0,a=e.length;r<a;r+=1){const a=e[r];if(a>99&&a<1e3||a>2050)return null;a>31&&(s+=1),a>12&&(t+=1),a<=0&&(n+=1)}return s>=2||3===t||n>=2?null:this.getDayMonth(e)}getDayMonth(e){const t=[[e[2],e.slice(0,2)],[e[0],e.slice(1,3)]],s=t.length;for(let n=0;n<s;n+=1){const[e,s]=t[n];if(1e3<=e&&e<=2050){const t=this.mapIntegersToDayMonth(s);return null!=t?{year:e,month:t.month,day:t.day}:null}}for(let n=0;n<s;n+=1){const[e,s]=t[n],r=this.mapIntegersToDayMonth(s);if(null!=r)return{year:this.twoToFourDigitYear(e),month:r.month,day:r.day}}return null}mapIntegersToDayMonth(e){const t=[e,e.slice().reverse()];for(let s=0;s<t.length;s+=1){const e=t[s],n=e[0],r=e[1];if(n>=1&&n<=31&&r>=1&&r<=12)return{day:n,month:r}}return null}twoToFourDigitYear(e){return e>99?e:e>50?e+1900:e+2e3}}const M=new Uint32Array(65536),x=(e,t)=>{if(e.length<t.length){const s=t;t=e,e=s}return 0===t.length?e.length:e.length<=32?((e,t)=>{const s=e.length,n=t.length,r=1<<s-1;let a=-1,o=0,i=s,c=s;for(;c--;)M[e.charCodeAt(c)]|=1<<c;for(c=0;c<n;c++){let e=M[t.charCodeAt(c)];const s=e|o;e|=(e&a)+a^a,o|=~(e|a),a&=e,o&r&&i++,a&r&&i--,o=o<<1|1,a=a<<1|~(s|o),o&=s}for(c=s;c--;)M[e.charCodeAt(c)]=0;return i})(e,t):((e,t)=>{const s=t.length,n=e.length,r=[],a=[],o=Math.ceil(s/32),i=Math.ceil(n/32);for(let p=0;p<o;p++)a[p]=-1,r[p]=0;let c=0;for(;c<i-1;c++){let o=0,i=-1;const l=32*c,h=Math.min(32,n)+l;for(let t=l;t<h;t++)M[e.charCodeAt(t)]|=1<<t;for(let e=0;e<s;e++){const s=M[t.charCodeAt(e)],n=a[e/32|0]>>>e&1,c=r[e/32|0]>>>e&1,l=s|o,h=((s|c)&i)+i^i|s|c;let u=o|~(h|i),d=i&h;u>>>31^n&&(a[e/32|0]^=1<<e),d>>>31^c&&(r[e/32|0]^=1<<e),u=u<<1|n,d=d<<1|c,i=d|~(l|u),o=u&l}for(let t=l;t<h;t++)M[e.charCodeAt(t)]=0}let l=0,h=-1;const u=32*c,d=Math.min(32,n-u)+u;for(let p=u;p<d;p++)M[e.charCodeAt(p)]|=1<<p;let g=n;for(let p=0;p<s;p++){const e=M[t.charCodeAt(p)],s=a[p/32|0]>>>p&1,o=r[p/32|0]>>>p&1,i=e|l,c=((e|o)&h)+h^h|e|o;let u=l|~(c|h),d=h&c;g+=u>>>n-1&1,g-=d>>>n-1&1,u>>>31^s&&(a[p/32|0]^=1<<p),d>>>31^o&&(r[p/32|0]^=1<<p),u=u<<1|s,d=d<<1|o,h=d|~(i|u),l=u&i}for(let p=u;p<d;p++)M[e.charCodeAt(p)]=0;return g})(e,t)},T=(e,t,s)=>{let n=0;const r=Object.keys(t).find((t=>{const r=((e,t,s)=>{const n=e.length<=t.length,r=e.length<=s;return n||r?Math.ceil(e.length/4):s})(e,t,s),a=x(e,t),o=a<=r;return o&&(n=a),o}));return r?{levenshteinDistance:n,levenshteinDistanceEntry:r}:{}};var S={a:["4","@"],b:["8"],c:["(","{","[","<"],e:["3"],g:["6","9"],i:["1","!","|"],l:["1","|","7"],o:["0"],s:["$","5"],t:["+","7"],x:["%"],z:["2"]},j={warnings:{straightRow:"straightRow",keyPattern:"keyPattern",simpleRepeat:"simpleRepeat",extendedRepeat:"extendedRepeat",sequences:"sequences",recentYears:"recentYears",dates:"dates",topTen:"topTen",topHundred:"topHundred",common:"common",similarToCommon:"similarToCommon",wordByItself:"wordByItself",namesByThemselves:"namesByThemselves",commonNames:"commonNames",userInputs:"userInputs",pwned:"pwned"},suggestions:{l33t:"l33t",reverseWords:"reverseWords",allUppercase:"allUppercase",capitalization:"capitalization",dates:"dates",recentYears:"recentYears",associatedYears:"associatedYears",sequences:"sequences",repeated:"repeated",longerKeyboardPattern:"longerKeyboardPattern",anotherWord:"anotherWord",useWords:"useWords",noNeed:"noNeed",pwned:"pwned"},timeEstimation:{ltSecond:"ltSecond",second:"second",seconds:"seconds",minute:"minute",minutes:"minutes",hour:"hour",hours:"hours",day:"day",days:"days",month:"month",months:"months",year:"year",years:"years",centuries:"centuries"}};const v=new class{constructor(){this.matchers={},this.l33tTable=S,this.dictionary={userInputs:[]},this.rankedDictionaries={},this.rankedDictionariesMaxWordSize={},this.translations=j,this.graphs={},this.useLevenshteinDistance=!1,this.levenshteinThreshold=2,this.l33tMaxSubstitutions=100,this.maxLength=256,this.setRankedDictionaries()}setOptions(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};e.l33tTable&&(this.l33tTable=e.l33tTable),e.dictionary&&(this.dictionary=e.dictionary,this.setRankedDictionaries()),e.translations&&this.setTranslations(e.translations),e.graphs&&(this.graphs=e.graphs),void 0!==e.useLevenshteinDistance&&(this.useLevenshteinDistance=e.useLevenshteinDistance),void 0!==e.levenshteinThreshold&&(this.levenshteinThreshold=e.levenshteinThreshold),void 0!==e.l33tMaxSubstitutions&&(this.l33tMaxSubstitutions=e.l33tMaxSubstitutions),void 0!==e.maxLength&&(this.maxLength=e.maxLength)}setTranslations(e){if(!this.checkCustomTranslations(e))throw new Error("Invalid translations object fallback to keys");this.translations=e}checkCustomTranslations(e){let t=!0;return Object.keys(j).forEach((s=>{if(s in e){const n=s;Object.keys(j[n]).forEach((s=>{s in e[n]||(t=!1)}))}else t=!1})),t}setRankedDictionaries(){const e={},t={};Object.keys(this.dictionary).forEach((s=>{e[s]=this.getRankedDictionary(s),t[s]=this.getRankedDictionariesMaxWordSize(s)})),this.rankedDictionaries=e,this.rankedDictionariesMaxWordSize=t}getRankedDictionariesMaxWordSize(e){const t=this.dictionary[e].map((e=>"string"!==typeof e?e.toString().length:e.length));return 0===t.length?0:t.reduce(((e,t)=>Math.max(e,t)),-1/0)}getRankedDictionary(e){const t=this.dictionary[e];if("userInputs"===e){const e=[];return t.forEach((t=>{const s=typeof t;"string"!==s&&"number"!==s&&"boolean"!==s||e.push(t.toString().toLowerCase())})),o(e)}return o(t)}extendUserInputsDictionary(e){this.dictionary.userInputs?this.dictionary.userInputs=[...this.dictionary.userInputs,...e]:this.dictionary.userInputs=e,this.rankedDictionaries.userInputs=this.getRankedDictionary("userInputs"),this.rankedDictionariesMaxWordSize.userInputs=this.getRankedDictionariesMaxWordSize("userInputs")}addMatcher(e,t){this.matchers[e]?console.info(`Matcher ${e} already exists`):this.matchers[e]=t}};class I{constructor(e){this.defaultMatch=e}match(e){let{password:t}=e;const s=t.split("").reverse().join("");return this.defaultMatch({password:s}).map((e=>({...e,token:e.token.split("").reverse().join(""),reversed:!0,i:t.length-1-e.j,j:t.length-1-e.i})))}}class D{constructor(e){this.defaultMatch=e}match(e){let{password:t}=e;const s=[],n=this.enumerateL33tSubs(this.relevantL33tSubtable(t,v.l33tTable)),a=Math.min(n.length,v.l33tMaxSubstitutions);for(let i=0;i<a;i+=1){const e=n[i];if(o=e,0===Object.keys(o).length)break;const a=r(t,e);this.defaultMatch({password:a}).forEach((n=>{const r=t.slice(n.i,+n.j+1||9e9);if(r.toLowerCase()!==n.matchedWord){const t={};Object.keys(e).forEach((s=>{const n=e[s];-1!==r.indexOf(s)&&(t[s]=n)}));const a=Object.keys(t).map((e=>`${e} -> ${t[e]}`)).join(", ");s.push({...n,l33t:!0,token:r,sub:t,subDisplay:a})}}))}var o;return s.filter((e=>e.token.length>1))}relevantL33tSubtable(e,t){const s={},n={};return e.split("").forEach((e=>{s[e]=!0})),Object.keys(t).forEach((e=>{const r=t[e].filter((e=>e in s));r.length>0&&(n[e]=r)})),n}enumerateL33tSubs(e){const t=Object.keys(e);return this.getSubs(t,[[]],e).map((e=>{const t={};return e.forEach((e=>{let[s,n]=e;t[s]=n})),t}))}getSubs(e,t,s){if(!e.length)return t;const n=e[0],r=e.slice(1),a=[];s[n].forEach((e=>{t.forEach((t=>{let s=-1;for(let n=0;n<t.length;n+=1)if(t[n][0]===e){s=n;break}if(-1===s){const s=t.concat([[e,n]]);a.push(s)}else{const r=t.slice(0);r.splice(s,1),r.push([e,n]),a.push(t),a.push(r)}}))}));const o=this.dedup(a);return r.length?this.getSubs(r,o,s):o}dedup(e){const t=[],s={};return e.forEach((e=>{const n=e.map(((e,t)=>[e,t]));n.sort();const r=n.map((e=>{let[t,s]=e;return`${t},${s}`})).join("-");r in s||(s[r]=!0,t.push(e))})),t}}class A{constructor(){this.l33t=new D(this.defaultMatch),this.reverse=new I(this.defaultMatch)}match(e){let{password:t}=e;const s=[...this.defaultMatch({password:t}),...this.reverse.match({password:t}),...this.l33t.match({password:t})];return a(s)}defaultMatch(e){let{password:t}=e;const s=[],n=t.length,r=t.toLowerCase();return Object.keys(v.rankedDictionaries).forEach((e=>{const a=v.rankedDictionaries[e],o=v.rankedDictionariesMaxWordSize[e],i=Math.min(o,n);for(let c=0;c<n;c+=1){const o=Math.min(c+i,n);for(let i=c;i<o;i+=1){const o=r.slice(c,+i+1||9e9),l=o in a;let h={};const u=0===c&&i===n-1;v.useLevenshteinDistance&&u&&!l&&(h=T(o,a,v.levenshteinThreshold));const d=0!==Object.keys(h).length;if(l||d){const n=a[d?h.levenshteinDistanceEntry:o];s.push({pattern:"dictionary",i:c,j:i,token:t.slice(c,+i+1||9e9),matchedWord:o,rank:n,dictionaryName:e,reversed:!1,l33t:!1,...h})}}}})),s}}class C{match(e){let{password:t,regexes:s=k}=e;const n=[];return Object.keys(s).forEach((e=>{const r=s[e];r.lastIndex=0;const a=r.exec(t);if(a){const t=a[0];n.push({pattern:"regex",token:t,i:a.index,j:a.index+a[0].length-1,regexName:e,regexMatch:a})}})),a(n)}}var E={nCk(e,t){let s=e;if(t>s)return 0;if(0===t)return 1;let n=1;for(let r=1;r<=t;r+=1)n*=s,n/=r,s-=1;return n},log10:e=>Math.log(e)/Math.log(10),log2:e=>Math.log(e)/Math.log(2),factorial(e){let t=1;for(let s=2;s<=e;s+=1)t*=s;return t}};var L=e=>{const t=e.replace(m,"");if(t.match(g)||t.toLowerCase()===t)return 1;const s=[c,l,u],n=s.length;for(let r=0;r<n;r+=1){const e=s[r];if(t.match(e))return 2}return(e=>{const t=e.split(""),s=t.filter((e=>e.match(f))).length,n=t.filter((e=>e.match(p))).length;let r=0;const a=Math.min(s,n);for(let o=1;o<=a;o+=1)r+=E.nCk(s+n,o);return r})(t)};const O=e=>{let{token:t,graph:s,turns:n}=e;const r=Object.keys(v.graphs[s]).length,a=(e=>{let t=0;return Object.keys(e).forEach((s=>{const n=e[s];t+=n.filter((e=>!!e)).length})),t/=Object.entries(e).length,t})(v.graphs[s]);let o=0;const i=t.length;for(let c=2;c<=i;c+=1){const e=Math.min(n,c-1);for(let t=1;t<=e;t+=1)o+=E.nCk(c-1,t-1)*r*a**t}return o};const P={bruteforce:e=>{let t,{token:s}=e,n=10**s.length;return n===Number.POSITIVE_INFINITY&&(n=Number.MAX_VALUE),t=1===s.length?11:51,Math.max(n,t)},date:e=>{let{year:t,separator:s}=e;let n=365*Math.max(Math.abs(t-y),20);return s&&(n*=4),n},dictionary:e=>{let{rank:t,reversed:s,l33t:n,sub:r,token:a}=e;const o=t,i=L(a),c=(e=>{let{l33t:t,sub:s,token:n}=e;if(!t)return 1;let r=1;const a=s;return Object.keys(a).forEach((e=>{const{subbedCount:t,unsubbedCount:s}=(e=>{let{subs:t,subbed:s,token:n}=e;const r=t[s],a=n.toLowerCase().split("");return{subbedCount:a.filter((e=>e===s)).length,unsubbedCount:a.filter((e=>e===r)).length}})({subs:a,subbed:e,token:n});if(0===t||0===s)r*=2;else{const e=Math.min(s,t);let n=0;for(let r=1;r<=e;r+=1)n+=E.nCk(s+t,r);r*=n}})),r})({l33t:n,sub:r,token:a});return{baseGuesses:o,uppercaseVariations:i,l33tVariations:c,calculation:o*i*c*(s?2:1)}},regex:e=>{let{regexName:t,regexMatch:s,token:n}=e;const r={alphaLower:26,alphaUpper:26,alpha:52,alphanumeric:62,digits:10,symbols:33};return t in r?r[t]**n.length:"recentYear"===t?Math.max(Math.abs(parseInt(s[0],10)-y),20):0},repeat:e=>{let{baseGuesses:t,repeatCount:s}=e;return t*s},sequence:e=>{let{token:t,ascending:s}=e;const n=t.charAt(0);let r=0;return r=["a","A","z","Z","0","1","9"].includes(n)?4:n.match(/\d/)?10:26,s||(r*=2),r*t.length},spatial:e=>{let{graph:t,token:s,shiftedCount:n,turns:r}=e,a=O({token:s,graph:t,turns:r});if(n){const e=s.length-n;if(0===n||0===e)a*=2;else{let t=0;for(let s=1;s<=Math.min(n,e);s+=1)t+=E.nCk(n+e,s);a*=t}}return Math.round(a)}};var q=(e,t)=>{const s={};if("guesses"in e&&null!=e.guesses)return e;const n=((e,t)=>{let s=1;return e.token.length<t.length&&(s=1===e.token.length?10:50),s})(e,t),r=((e,t)=>P[e]?P[e](t):v.matchers[e]&&"scoring"in v.matchers[e]?v.matchers[e].scoring(t):0)(e.pattern,e);let a=0;"number"===typeof r?a=r:"dictionary"===e.pattern&&(a=r.calculation,s.baseGuesses=r.baseGuesses,s.uppercaseVariations=r.uppercaseVariations,s.l33tVariations=r.l33tVariations);const o=Math.max(a,n);return{...e,...s,guesses:o,guessesLog10:E.log10(o)}};const N={password:"",optimal:{},excludeAdditive:!1,fillArray(e,t){const s=[];for(let n=0;n<e;n+=1){let e=[];"object"===t&&(e={}),s.push(e)}return s},makeBruteforceMatch(e,t){return{pattern:"bruteforce",token:this.password.slice(e,+t+1||9e9),i:e,j:t}},update(e,t){const s=e.j,n=q(e,this.password);let r=n.guesses;t>1&&(r*=this.optimal.pi[n.i-1][t-1]);let a=E.factorial(t)*r;this.excludeAdditive||(a+=1e4**(t-1));let o=!1;Object.keys(this.optimal.g[s]).forEach((e=>{const n=this.optimal.g[s][e];parseInt(e,10)<=t&&n<=a&&(o=!0)})),o||(this.optimal.g[s][t]=a,this.optimal.m[s][t]=n,this.optimal.pi[s][t]=r)},bruteforceUpdate(e){let t=this.makeBruteforceMatch(0,e);this.update(t,1);for(let s=1;s<=e;s+=1){t=this.makeBruteforceMatch(s,e);const n=this.optimal.m[s-1];Object.keys(n).forEach((e=>{"bruteforce"!==n[e].pattern&&this.update(t,parseInt(e,10)+1)}))}},unwind(e){const t=[];let s=e-1,n=0,r=Infinity;const a=this.optimal.g[s];for(a&&Object.keys(a).forEach((e=>{const t=a[e];t<r&&(n=parseInt(e,10),r=t)}));s>=0;){const e=this.optimal.m[s][n];t.unshift(e),s=e.i-1,n-=1}return t}};var W={mostGuessableMatchSequence(e,t){let s=arguments.length>2&&void 0!==arguments[2]&&arguments[2];N.password=e,N.excludeAdditive=s;const n=e.length;let r=N.fillArray(n,"array");t.forEach((e=>{r[e.j].push(e)})),r=r.map((e=>e.sort(((e,t)=>e.i-t.i)))),N.optimal={m:N.fillArray(n,"object"),pi:N.fillArray(n,"object"),g:N.fillArray(n,"object")};for(let c=0;c<n;c+=1)r[c].forEach((e=>{e.i>0?Object.keys(N.optimal.m[e.i-1]).forEach((t=>{N.update(e,parseInt(t,10)+1)})):N.update(e,1)})),N.bruteforceUpdate(c);const a=N.unwind(n),o=a.length,i=this.getGuesses(e,o);return{password:e,guesses:i,guessesLog10:E.log10(i),sequence:a}},getGuesses(e,t){const s=e.length;let n=0;return n=0===e.length?1:N.optimal.g[s-1][t],n}};class z{match(e){let{password:t,omniMatch:s}=e;const n=[];let r=0;for(;r<t.length;){const e=this.getGreedyMatch(t,r),a=this.getLazyMatch(t,r);if(null==e)break;const{match:o,baseToken:i}=this.setMatchToken(e,a);if(o){const e=o.index+o[0].length-1,t=this.getBaseGuesses(i,s);n.push(this.normalizeMatch(i,e,o,t)),r=e+1}}return n.some((e=>e instanceof Promise))?Promise.all(n):n}normalizeMatch(e,t,s,n){const r={pattern:"repeat",i:s.index,j:t,token:s[0],baseToken:e,baseGuesses:0,repeatCount:s[0].length/e.length};return n instanceof Promise?n.then((e=>({...r,baseGuesses:e}))):{...r,baseGuesses:n}}getGreedyMatch(e,t){const s=/(.+)\1+/g;return s.lastIndex=t,s.exec(e)}getLazyMatch(e,t){const s=/(.+?)\1+/g;return s.lastIndex=t,s.exec(e)}setMatchToken(e,t){const s=/^(.+?)\1+$/;let n,r="";if(t&&e[0].length>t[0].length){n=e;const t=s.exec(n[0]);t&&(r=t[1])}else n=t,n&&(r=n[1]);return{match:n,baseToken:r}}getBaseGuesses(e,t){const s=t.match(e);if(s instanceof Promise)return s.then((t=>W.mostGuessableMatchSequence(e,t).guesses));return W.mostGuessableMatchSequence(e,s).guesses}}class R{constructor(){this.MAX_DELTA=5}match(e){let{password:t}=e;const s=[];if(1===t.length)return[];let n=0,r=null;const a=t.length;for(let o=1;o<a;o+=1){const e=t.charCodeAt(o)-t.charCodeAt(o-1);if(null==r&&(r=e),e!==r){const a=o-1;this.update({i:n,j:a,delta:r,password:t,result:s}),n=a,r=e}}return this.update({i:n,j:a-1,delta:r,password:t,result:s}),s}update(e){let{i:t,j:s,delta:n,password:r,result:a}=e;if(s-t>1||1===Math.abs(n)){const e=Math.abs(n);if(e>0&&e<=this.MAX_DELTA){const e=r.slice(t,+s+1||9e9),{sequenceName:o,sequenceSpace:i}=this.getSequence(e);return a.push({pattern:"sequence",i:t,j:s,token:r.slice(t,+s+1||9e9),sequenceName:o,sequenceSpace:i,ascending:n>0})}}return null}getSequence(e){let t="unicode",s=26;return d.test(e)?(t="lower",s=26):h.test(e)?(t="upper",s=26):b.test(e)&&(t="digits",s=10),{sequenceName:t,sequenceSpace:s}}}class Y{constructor(){this.SHIFTED_RX=/[~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?]/}match(e){let{password:t}=e;const s=[];return Object.keys(v.graphs).forEach((e=>{const r=v.graphs[e];n(s,this.helper(t,r,e))})),a(s)}checkIfShifted(e,t,s){return!e.includes("keypad")&&this.SHIFTED_RX.test(t.charAt(s))?1:0}helper(e,t,s){let n;const r=[];let a=0;const o=e.length;for(;a<o-1;){let i=a+1,c=0,l=0;for(n=this.checkIfShifted(s,e,a);;){const h=t[e.charAt(i-1)]||[];let u=!1,d=-1,g=-1;if(i<o){const t=e.charAt(i),s=h.length;for(let e=0;e<s;e+=1){const s=h[e];if(g+=1,s){const e=s.indexOf(t);if(-1!==e){u=!0,d=g,1===e&&(n+=1),c!==d&&(l+=1,c=d);break}}}}if(!u){i-a>2&&r.push({pattern:"spatial",i:a,j:i-1,token:e.slice(a,i),graph:s,turns:l,shiftedCount:n}),a=i;break}i+=1}}return r}}class G{constructor(){this.matchers={date:w,dictionary:A,regex:C,repeat:z,sequence:R,spatial:Y}}match(e){const t=[],s=[];return[...Object.keys(this.matchers),...Object.keys(v.matchers)].forEach((r=>{if(!this.matchers[r]&&!v.matchers[r])return;const a=(new(this.matchers[r]?this.matchers[r]:v.matchers[r].Matching)).match({password:e,omniMatch:this});a instanceof Promise?(a.then((e=>{n(t,e)})),s.push(a)):n(t,a)})),s.length>0?new Promise((e=>{Promise.all(s).then((()=>{e(a(t))}))})):a(t)}}const $=2678400,F=32140800,B={second:1,minute:60,hour:3600,day:86400,month:$,year:F,century:321408e4};class H{translate(e,t){let s=e;void 0!==t&&1!==t&&(s+="s");const{timeEstimation:n}=v.translations;return n[s].replace("{base}",`${t}`)}estimateAttackTimes(e){const t={onlineThrottling100PerHour:e/(100/3600),onlineNoThrottling10PerSecond:e/10,offlineSlowHashing1e4PerSecond:e/1e4,offlineFastHashing1e10PerSecond:e/1e10},s={onlineThrottling100PerHour:"",onlineNoThrottling10PerSecond:"",offlineSlowHashing1e4PerSecond:"",offlineFastHashing1e10PerSecond:""};return Object.keys(t).forEach((e=>{const n=t[e];s[e]=this.displayTime(n)})),{crackTimesSeconds:t,crackTimesDisplay:s,score:this.guessesToScore(e)}}guessesToScore(e){return e<1005?0:e<1000005?1:e<100000005?2:e<10000000005?3:4}displayTime(e){let t,s="centuries";const n=Object.keys(B),r=n.findIndex((t=>e<B[t]));return r>-1&&(s=n[r-1],0!==r?t=Math.round(e/B[s]):s="ltSecond"),this.translate(s,t)}}var U=()=>null,Z=()=>({warning:v.translations.warnings.dates,suggestions:[v.translations.suggestions.dates]});const V=(e,t)=>{let s="";const n=e.dictionaryName,r="lastnames"===n||n.toLowerCase().includes("firstnames");return"passwords"===n?s=((e,t)=>{let s="";return!t||e.l33t||e.reversed?e.guessesLog10<=4&&(s=v.translations.warnings.similarToCommon):s=e.rank<=10?v.translations.warnings.topTen:e.rank<=100?v.translations.warnings.topHundred:v.translations.warnings.common,s})(e,t):n.includes("wikipedia")?s=((e,t)=>{let s="";return t&&(s=v.translations.warnings.wordByItself),s})(0,t):r?s=((e,t)=>t?v.translations.warnings.namesByThemselves:v.translations.warnings.commonNames)(0,t):"userInputs"===n&&(s=v.translations.warnings.userInputs),s};var _=(e,t)=>{const s=V(e,t),n=[],r=e.token;return r.match(c)?n.push(v.translations.suggestions.capitalization):r.match(u)&&r.toLowerCase()!==r&&n.push(v.translations.suggestions.allUppercase),e.reversed&&e.token.length>=4&&n.push(v.translations.suggestions.reverseWords),e.l33t&&n.push(v.translations.suggestions.l33t),{warning:s,suggestions:n}},X=e=>"recentYear"===e.regexName?{warning:v.translations.warnings.recentYears,suggestions:[v.translations.suggestions.recentYears,v.translations.suggestions.associatedYears]}:{warning:"",suggestions:[]},K=e=>{let t=v.translations.warnings.extendedRepeat;return 1===e.baseToken.length&&(t=v.translations.warnings.simpleRepeat),{warning:t,suggestions:[v.translations.suggestions.repeated]}},J=()=>({warning:v.translations.warnings.sequences,suggestions:[v.translations.suggestions.sequences]}),Q=e=>{let t=v.translations.warnings.keyPattern;return 1===e.turns&&(t=v.translations.warnings.straightRow),{warning:t,suggestions:[v.translations.suggestions.longerKeyboardPattern]}};const ee={warning:"",suggestions:[]};class te{constructor(){this.matchers={bruteforce:U,date:Z,dictionary:_,regex:X,repeat:K,sequence:J,spatial:Q},this.defaultFeedback={warning:"",suggestions:[]},this.setDefaultSuggestions()}setDefaultSuggestions(){this.defaultFeedback.suggestions.push(v.translations.suggestions.useWords,v.translations.suggestions.noNeed)}getFeedback(e,t){if(0===t.length)return this.defaultFeedback;if(e>2)return ee;const s=v.translations.suggestions.anotherWord,n=this.getLongestMatch(t);let r=this.getMatchFeedback(n,1===t.length);return null!==r&&void 0!==r?(r.suggestions.unshift(s),null==r.warning&&(r.warning="")):r={warning:"",suggestions:[s]},r}getLongestMatch(e){let t=e[0];return e.slice(1).forEach((e=>{e.token.length>t.token.length&&(t=e)})),t}getMatchFeedback(e,t){return this.matchers[e.pattern]?this.matchers[e.pattern](e,t):v.matchers[e.pattern]&&"feedback"in v.matchers[e.pattern]?v.matchers[e.pattern].feedback(e,t):ee}}const se=()=>(new Date).getTime(),ne=(e,t,s)=>{const n=new te,r=new H,a=W.mostGuessableMatchSequence(t,e),o=se()-s,i=r.estimateAttackTimes(a.guesses);return{calcTime:o,...a,...i,feedback:n.getFeedback(i.score,a.sequence)}},re=(e,t)=>{t&&v.extendUserInputsDictionary(t);return(new G).match(e)},ae=e=>{let{password:t,username:n="",useLevenshteinDistance:r=!1}=e;const a=t?t.substring(0,50).replace(/\s/g,""):"",o=n?n.substring(0,50).toLowerCase():"";return(async()=>{const e=await s.e(228).then(s.bind(s,90314)),t=await s.e(95).then(s.bind(s,78093)),n=await s.e(899).then(s.bind(s,98632)),r=await s.e(71).then(s.bind(s,9895)),a=await s.e(381).then(s.bind(s,58581)),o=await s.e(889).then(s.bind(s,1982)),i=await s.e(508).then(s.bind(s,12972)),c=await s.e(393).then(s.bind(s,5873));return{dictionary:{...e.default.dictionary,...t.default.dictionary,...n.default.dictionary,...r.default.dictionary,...a.default.dictionary,...o.default.dictionary,...i.default.dictionary,...c.default.dictionary},graphs:e.default.adjacencyGraphs,translations:t.default.translations}})().then((e=>{v.setOptions({...e,useLevenshteinDistance:r})})),25*((e,t)=>{const s=se(),n=re(e,t);if(n instanceof Promise)throw new Error("You are using a Promised matcher, please use `zxcvbnAsync` for it.");return ne(n,e,s)})(a,[o,"lastpass","lastpass.com"]).score}}}]);