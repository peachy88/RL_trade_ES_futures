�%  *)\����@�(\�"	�@2�
tIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2�Ӿ��z'@!�ʵ�vD@)Ӿ��z'@1�ʵ�vD@:Preprocessing2�
JIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map�%��ڄ @!*�TJ=@)�辜Q @1]��
4�<@:Preprocessing2�
�Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelMapV2::AssertCardinality::ParallelInterleaveV4���'�8@!-�X��#@)��'�8@1-�X��#@:Preprocessing2�
�Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelMapV2��ME*�m�?!M�����@)�ME*�m�?1M�����@:Preprocessing2�
�Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelMapV2::AssertCardinality��}���@!��Oa�E)@)�L���$�?1�??J@:Preprocessing2T
Iterator::Prefetch::Generator����K��?!·�Q(@)����K��?1·�Q(@:Preprocessing2�
�Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelMapV2::AssertCardinality::ParallelInterleaveV4[0]::FlatMap�NB�!��?!�q�M�@)y�'eR�?1eɥ�@:Preprocessing2�
eIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl�hz��LW(@!��x�D�E@)I��-�?1L/L�@:Preprocessing2�
�Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelMapV2::AssertCardinality::ParallelInterleaveV4[0]::FlatMap[0]::TFRecord�$0��{�?!���:�?)$0��{�?1���:�?:Advanced file read2b
+Iterator::Model::Prefetch::Rebatch::BatchV2f��
b @!����U=@)YO���*�?1��b͉�?:Preprocessing2�
aIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCache�-'���(@!� 
�F@)���b('�?1zq��i�?:Preprocessing2l
4Iterator::Model::Prefetch::Rebatch::BatchV2::Shuffle��S�q�!@!�T"�u?@){Cr2�?1[wb�t�?:Preprocessing2}
EIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl�IG9�M� @!��NI4�=@)"�^F���?1�/��D�?:Preprocessing2y
AIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCache���G�!@!8Ag=�L>@)DN_��,�?1��}�?:Preprocessing2�
TIterator::Model::Prefetch::Rebatch::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch����
��?!��IҶ�?)���
��?1��IҶ�?:Preprocessing2F
Iterator::Model�9�!�?! U��,�?)��D���?1�4�l�2�?:Preprocessing2Y
"Iterator::Model::Prefetch::Rebatch�k�6f @!���,�=@)LqU�wE�?1Z���ٜ?:Preprocessing2I
Iterator::Prefetch�1>�^�}?!_�N@QW�?)�1>�^�}?1_�N@QW�?:Preprocessing2P
Iterator::Model::Prefetch�-���o?!"��"MM�?)�-���o?1"��"MM�?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysisg
unknownTNo step time measured. Therefore we cannot tell where the performance bottleneck is.no*no#You may skip the rest of this page.BX
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown
  " * 2 : B J R Z JGPUb��No step marker observed and hence the step time is unknown. This may happen if (1) training steps are not instrumented (e.g., if you are not using Keras) or (2) the profiling duration is shorter than the step time. For (1), you need to add step instrumentation; for (2), you may try to profile longer.Y      Y@qLU�`��@"�
unknownTNo step time measured. Therefore we cannot tell where the performance bottleneck is.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"O
Mtensorflow_stats (identify the time-consuming operations executed on the GPU)"U
Strace_viewer (look at the activities on the timeline of each GPU in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2I
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono:
Refer to the TF2 Profiler FAQ2"GPU(: B��No step marker observed and hence the step time is unknown. This may happen if (1) training steps are not instrumented (e.g., if you are not using Keras) or (2) the profiling duration is shorter than the step time. For (1), you need to add step instrumentation; for (2), you may try to profile longer.Malex-Mant: Insufficient privilege to run libcupti (you need root permission).