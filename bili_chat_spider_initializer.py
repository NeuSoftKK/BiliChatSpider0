import json
import logging
import os


def init_config():
    config_path = './config/chat_spider_config.json'
    if not os.path.exists(config_path):
        raise FileNotFoundError(f'Can not find configuration file in directory "{config_path}".')

    with open(file=config_path, encoding='utf-8', mode='r') as file:
        config = json.load(fp=file)

    max_parallel_job_num = config['max_parallel_job_num']
    if max_parallel_job_num > 36:
        logging.warning(
            f'Argument "max_parallel_job_num" was set to {max_parallel_job_num} and this may cause your system crash.')

    sleep_time_before_job_launching = config['sleep_time_before_job_launching']
    if sleep_time_before_job_launching > 60:
        logging.warning(
            f'Argument "sleep_time_before_job_launching" was set to {sleep_time_before_job_launching} and this may cause long time waiting.')

    sleep_time_after_job_launching = config['sleep_time_after_job_launching']
    if sleep_time_after_job_launching > 60:
        logging.warning(
            f'Argument "sleep_time_after_job_launching" was set to {sleep_time_after_job_launching} and this may cause long time waiting.')

    save_path = config['save_path']
    if not os.path.exists(save_path):
        logging.error(f'Argument "save_path" was set to "{save_path}" and it is not an accessible nor valid directory.')
        raise NotADirectoryError()

    firefox_profile_dir = config['firefox_profile_dir']
    if not os.path.exists(firefox_profile_dir):
        logging.warning(
            f'Argument "firefox_profile_dir" was set to "{firefox_profile_dir}" and it is not an accessible nor valid '
            f'directory. This may cause selenium can not found sufficient replies from your web browser when your '
            f'login-info can not be pertained.')

    firefox_driver_dir = config['firefox_driver_dir']
    if not os.path.exists(firefox_driver_dir):
        logging.error(
            f'Argument "firefox_driver_dir" was set to "{firefox_driver_dir}" and it is not an accessible nor valid directory. Without setting a proper path, selenium can not start successfully.')
        raise NotADirectoryError()

    return config
