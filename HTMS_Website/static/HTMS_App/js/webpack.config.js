const path = require('path');

module.exports = {
    // mode: 'development',

    // watch: true,
    // entry: {
    //     controller: path.resolve(__dirname, "src/js/controller.js"),
    // },
    // output: {
    //     path: path.resolve(__dirname, "../"),
    //     filename: "index.js",
    //     clean: true,
    // },
    // devtool: 'source-map',
    // module: {
    //     rules: [
    //         {
    //             test: /\.js$/,
    //             exclude: /node_modules/,
    //             use: {
    //                 loader: 'babel-loader',
    //                 options: {
    //                     presets: ['@babel/preset-env'],
    //                 },
    //             }
    //         }]
    // },



    mode: 'production',
    entry: {
        controller: path.resolve(__dirname, "src/js/controller.js"),
        login: path.resolve(__dirname, "src/js/login_page.js"),
    },
    output: {
        path: path.resolve(__dirname, "../"),
        filename: "[name].js",
        chunkFilename: "[id].[name].js",
        publicPath: "/",
    },

    devtool: false,
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                }
            }
        ]
    },
    optimization: {
        minimize: true,
    }


    ///////////////////////////////////
    // add assets
    //////////////////////////////

    // module.exports = {
    //     mode: 'development',
    //     watch: true,
    //     entry: {
    //         controller: path.resolve(__dirname, "src/js/new_assets.js"),
    //     },
    //     output: {
    //         path: path.resolve(__dirname, "../"),
    //         filename: "new_assets.js",
    //         // clean: true,
    //     },
    //     devtool: 'source-map',
    //     module: {
    //         rules: [
    //             {
    //                 test: /\.js$/,
    //                 exclude: /node_modules/,
    //                 use: {
    //                     loader: 'babel-loader',
    //                     options: {
    //                         presets: ['@babel/preset-env'],
    //                     },
    //                 }
    //             }]
    //     },
    // module.exports = {
    //     mode: 'development',
    //     watch: true,
    //     entry: {
    //         controller: path.resolve(__dirname, "src/js/login_page.js"),
    //     },
    //     output: {
    //         path: path.resolve(__dirname, "../"),
    //         filename: "login_page.js",
    //         clean: true,
    //     },
    //     devtool: 'source-map',
    //     module: {
    //         rules: [
    //             {
    //                 test: /\.js$/,
    //                 exclude: /node_modules/,
    //                 use: {
    //                     loader: 'babel-loader',
    //                     options: {
    //                         presets: ['@babel/preset-env'],
    //                     },
    //                 }
    //             }]
    //     },
    // resolve: {
    //     fallback: {
    //         // url: require.resolve('url'),
    //         fs: false,
    //         dns: false,
    //         net: false,
    //         tls: false,
    //         // assert: require.resolve('assert'),
    //         crypto: require.resolve('crypto-browserify'),
    //         // http: require.resolve('stream-http'),
    //         // https: require.resolve('https-browserify'),
    //         // os: require.resolve('os-browserify/browser'),
    //         // buffer: require.resolve('buffer'),
    //         stream: require.resolve('stream-browserify'),
    //         // assert: require.resolve('assert'),
    //         // buffer: require.resolve('buffer'),
    //         // console: require.resolve('console-browserify'),
    //         // constants: require.resolve('constants-browserify'),
    //         // domain: require.resolve('domain-browser'),
    //         // events: require.resolve('events'),
    //         // http: require.resolve('stream-http'),
    //         // https: require.resolve('https-browserify'),
    //         // os: require.resolve('os-browserify/browser'),
    //         path: require.resolve('path-browserify'),
    //         // punycode: require.resolve('punycode'),
    //         // process: require.resolve('process/browser'),
    //         // querystring: require.resolve('querystring-es3'),
    //         // string_decoder: require.resolve('string_decoder'),
    //         // sys: require.resolve('util'),
    //         // timers: require.resolve('timers-browserify'),
    //         // tty: require.resolve('tty-browserify'),
    //         // url: require.resolve('url'),
    //         // util: require.resolve('util'),
    //         // vm: require.resolve('vm-browserify'),
    //         // zlib: require.resolve('browserify-zlib'),

    //     },
    //     alias: {
    //         'pg-native': path.join(__dirname, 'alias/pg-native.js'),
    //         'pgpass$': path.join(__dirname, 'alias/pgpass.js'),
    //     },

    // },

    // target: 'node',
}